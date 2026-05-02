import cv2
import time
import socket

#classificador de rosto ta lá no git do OpenCv, mas deve ta ae nos arquivos
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#pegar IP da máquina
ip = socket.gethostbyname(socket.gethostname())
print("IP da máquina:", ip)

#abri a câmera
camera = cv2.VideoCapture(0)

foto_tirada = False
for i in range(5):
    while True:

        ret, frame = camera.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #detecta rostos
        faces = face.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            #desenha um quadrado no rosto
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

            #tira foto apenas uma vez
            if not foto_tirada:
                #dados de data e hora de quando a foto foi tirada
                dat_hr = f"data_{time.strftime('%Y-%m-%d')}_hora_{time.strftime('%H-%M-%S')}.jpg"

                #add filtro de redução de ruído:
                frame = cv2.medianBlur(frame, 5)

                #salva a imagem com esse nome ae e adiciona o ip da máquina e os dados de data e hora
                cv2.imwrite(f"rosto_detectado_{ip}_{dat_hr}", frame)

                foto_tirada = True

        cv2.imshow("Camera", frame)

        #isso aqui é pra caso não reconheça o rosto, apertando a tecla Q uma foto pode ser tirada
        if cv2.waitKey(1) == ord("q"):
            cv2.imwrite("Sem rosto.png", frame)
            foto_tirada = True
            break

#to com preguiça enfim só dar ctrl C no terminal pra matar o processo
camera.release()
cv2.destroyAllWindows()

#observação: eu tive essa ideia devido aquela funcionalidade das camêras dos celulares que tiram foto assim que tem um rosto enquadrado ou quando mostram a mão (não programei a da mão ainda mas irei)