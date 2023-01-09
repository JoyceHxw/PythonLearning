import math
import cv2
import mediapipe as mp
import pyautogui as ui
ui.FAILSAFE = False
# ui.PAUSE = 1 
import time
import os
import pyttsx3



class HandNumber():
    def __init__(self) -> None:
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.mp_holistic=mp.solutions.holistic
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.cnt1=0   # 切换模式
        self.cnt2=0   # 是否识别手势（防止误触）
        self.remind=pyttsx3.init()    # 模式切换提示声音

    def get_distance(self,x,y):
        return round(math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2),2)
    
    def number_control(self,number):
        # 控制视频播放
        if number==10:
            self.cnt2+=1
            time.sleep(1)
            if self.cnt2%2==0:
                self.remind.say("开始手势控制")
                self.remind.runAndWait()
                print("开始手势控制")
            else:
                self.remind.say("暂停手势控制")
                self.remind.runAndWait()
                print("暂停手势控制")
        if self.cnt2%2==0:
            if number==1:
                ui.press('space')
                print("暂停/播放")
                time.sleep(1)
            elif number==2:     
                ui.press('right')
                print("快进")
            elif number==3:     
                ui.press('left')
                print("快退")
            elif number==4:  
                ui.press('volumeup')   
                print("提高音量")
            elif number==5:  
                ui.press('volumedown')   
                print("降低音量")
        else:
            pass 

    def number_reg(self,results,image):
        number=0 # 显式数字
        if results.multi_hand_landmarks:  # 识别出的所有手的手部的所有信息点
            # landmark表示每个信息点中有三个参数 x y z。
            # 要注意的是x,y是小数，是相对整个屏幕到左侧和上侧的距离，若为0，那么手指在屏幕左侧边缘，若为1，那么信息点在屏幕右侧边缘。
            # y方向同理。z为以手腕处为原点，距相机的距离，值越小表示地标离相机越近
            for hand_landmarks in results.multi_hand_landmarks:  # 几只手
                self.mp_drawing.draw_landmarks(image, hand_landmarks,self.mp_hands.HAND_CONNECTIONS)
                origin1=(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y, hand_landmarks.landmark[0].z)  # 其他手指的原点
                origin2=(hand_landmarks.landmark[17].x, hand_landmarks.landmark[17].y, hand_landmarks.landmark[17].z) # 大拇指的原点
                distance_base1=self.get_distance((hand_landmarks.landmark[9].x,hand_landmarks.landmark[9].y,hand_landmarks.landmark[9].z),origin1)  # 其他手指的参考值（不受距离影响）
                distance_base2=self.get_distance((hand_landmarks.landmark[2].x,hand_landmarks.landmark[2].y,hand_landmarks.landmark[2].z),origin2)  # 大拇指的参考值
                for i, landmark in enumerate(hand_landmarks.landmark):  # 一只手上的信息点
                    # 大拇指
                    if i==4:
                        point=(landmark.x, landmark.y, landmark.z)
                        if self.get_distance(point,origin2)>=distance_base2*1.1:
                            number+=1
                    # 其他手指
                    if i in (8,12,16,20):
                        point=(landmark.x, landmark.y, landmark.z)
                        if self.get_distance(point,origin1)>=distance_base1*1.2:
                            number+=1
        image=cv2.flip(image,1)   # 由于是自拍，所以水平翻转
        cv2.putText(image,f"Number: {number} ",(50,50),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),3)
        cv2.imwrite(str(os.getcwd()).replace("\\","/")+"/"+"result.png", image)  
        cv2.imshow('MediaPipe Hands', image)  # 不显式，展示视频播放器

        self.number_control(number)


    def mouse_reg(self,cap,results,image):
        c_width,c_height = ui.size()    # 显式器大小
        v_width,v_height=cap.get(3),cap.get(4)    # 弹出窗口大小
        ratio1=c_width/c_height   # 显示器长宽比例
        r_width_min=int((v_width-v_height/1.5*ratio1)/2)    # 提示框位置
        r_height_min=int((v_height-v_height/1.5)/3)
        r_width_max=int(r_width_min+v_height/1.5*ratio1)
        r_height_max=int(r_height_min+v_height/1.5)
        cv2.rectangle(image,(r_width_min,r_height_min),(r_width_max,r_height_max),(0,0,255),5)

        if results.multi_hand_landmarks:  # 识别出的所有手的手部的所有信息点
            hand_landmarks=results.multi_hand_landmarks[0]  # 一只手
            self.mp_drawing.draw_landmarks(image, hand_landmarks,self.mp_hands.HAND_CONNECTIONS)
            distances=[]
            positions=[]
            origin1=(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y, hand_landmarks.landmark[0].z)  # 其他手指的原点
            origin2=(hand_landmarks.landmark[17].x, hand_landmarks.landmark[17].y, hand_landmarks.landmark[17].z) # 大拇指的原点
            distance_base1=self.get_distance((hand_landmarks.landmark[9].x,hand_landmarks.landmark[9].y,hand_landmarks.landmark[9].z),origin1)  # 其他手指的参考值（不受距离影响）
            distance_base2=self.get_distance((hand_landmarks.landmark[2].x,hand_landmarks.landmark[2].y,hand_landmarks.landmark[2].z),origin2)  # 大拇指的参考值
            for id,landmark in enumerate(hand_landmarks.landmark):  # 一只手上的信息点
                point=(landmark.x, landmark.y, landmark.z)
                positions.append(point)
                if id==4:
                    distance=self.get_distance(point,origin2)
                else:
                    distance=self.get_distance(point,origin1)
                distances.append(distance)

            if distances[4]>=distance_base2*1.1 and min(distances[x] for x in (8,12,16,20)) >= distance_base1*1.2:
                self.cnt2+=1
                time.sleep(1)
                if self.cnt2%2==0:
                    self.remind.say("开始手势控制")
                    self.remind.runAndWait()
                    print("开始手势控制")
                else:
                    self.remind.say("暂停手势控制")
                    self.remind.runAndWait()
                    print("暂停手势控制")
            
            if self.cnt2%2==0:
                # 鼠标移动
                if max(distances)==distances[8]:
                    w=c_width-(positions[8][0]*v_width-r_width_min)/(v_height/1.5*ratio1)*c_width
                    h=(positions[8][1]*v_height-r_height_min)/(v_height/1.5)*c_height
                    ui.moveTo(w, h,duration=0.001)   # 手在屏幕下方可能无法识别，所以乘以参数
                    # 鼠标点击
                    if self.get_distance(positions[4],origin2)>=distance_base2*1.1:
                        # ui.mouseDown(x=c_width-positions[8][0]*c_width*1.3,y=positions[8][1]*c_height*1.3,button='left',duration=0.001)
                        ui.click(x=w,y=h,button='left')
                        print("点击")
                        time.sleep(0.5)
        image=cv2.flip(image,1)   # 由于是自拍，所以水平翻转
        cv2.putText(image,"Please move inside the red box",(50,50),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),3)
        cv2.imwrite(str(os.getcwd()).replace("\\","/")+"/"+"result.png", image)  
        cv2.imshow('MediaPipe Hands', image) 


    def choose_mode(self):
        cap=cv2.VideoCapture(0)   # 弹出窗口获取用户摄像头权限
        cap.set(3,1280)   # 图像比例
        cap.set(4,720)
        self.cnt1=0
        with self.mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
            with self.mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
                while cap.isOpened():
                    # cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。
                    # 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。
                    # frame就是每一帧的图像，是个三维矩阵
                    success, image = cap.read()  
                    if not success:
                        print("Ignoring empty camera frame.")
                        continue

                    image.flags.writeable = False  # 提高图片处理性能
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换成RGB格式
                    results1 = holistic.process(image)
                    results2 = hands.process(image)

                    image.flags.writeable = True  # 对图片进行标注
                    image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    if results1.pose_landmarks:
                        # self.mp_drawing.draw_landmarks(
                        #     image,
                        #     results1.face_landmarks,
                        #     self.mp_holistic.FACEMESH_CONTOURS,
                        #     landmark_drawing_spec=None,
                        #     connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_contours_style())
                        self.mp_drawing.draw_landmarks(
                            image,
                            results1.pose_landmarks,
                            self.mp_holistic.POSE_CONNECTIONS,
                            landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())

                        if results1.pose_landmarks.landmark[13].y<results1.pose_landmarks.landmark[11].y and results1.pose_landmarks.landmark[14].y<results1.pose_landmarks.landmark[12].y:
                            self.cnt1+=1
                            self.cnt2=0
                            time.sleep(1)
                            print("切换模式")
                            self.remind.say("切换模式")
                            self.remind.runAndWait()

                    
                    if self.cnt1%2==0:
                        # print("键盘模式")
                        self.number_reg(results2,image)
                    else:
                        # print("鼠标模式")
                        self.mouse_reg(cap,results2,image)

                    if cv2.waitKey(5) & 0xFF == 27:
                        break

        cap.release()

HN=HandNumber()
HN.choose_mode()
