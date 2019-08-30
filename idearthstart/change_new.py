import sense

def parsing(bhumidity,btemperature):
    emotionlist = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']

    with open('/home/pi/wget-3.2/output.txt') as file:
        string = file.readlines()
        #temperature = sense.getTemperature()
        light = sense.getLight()
        #print("change light")
        humidity, temperature =bhumidity, btemperature
        #if count % 5 ==0:
        #    humidity, temperature = sense.getHumidityTemperature()
        #else:
        #    humidity, temperature = bhumidity,btemperature
        #print("chagne humidity, temperature")
        sound = sense.getSound()
        #print("change sound")
        f=open('/home/pi/RpiSetup/remote_control/remote_control/templates/templates/output.html','w')
        p=open('/home/pi/wget-3.2/php.txt','w')
        f.write('{')
        p.write('{')
        if temperature != -1:
            try:
                f.write('"temperature":"%f",'%temperature)
                p.write('"temperature":"%f",'%temperature)
            except:
                f.write('"temperature":-1.000000,')
                p.write('"temperature":-1.000000,')
        if light != -1:
            f.write('"light":"%f",'%light)
            p.write('"light":"%f",'%light)
        if humidity != -1:
            try:
                f.write('"humidity":"%f",'%humidity)
                p.write('"humidity":"%f",'%humidity)
            except:
                f.write('"humidity":-1.000000,')
                p.write('"humidity":-1.000000,')
        if sound != -1:
            f.write('"sound":"%f"'%sound)
            p.write('"sound":"%f"'%sound)
        
        for emotion in emotionlist:
            try:    
                result = [',"']
                result.append(emotion)
                result.append('":"')

                num = string[0].find(emotion)+len(emotion)+3
                result.append(string[0][num:num+2])
                num += 2
                while(string[0][num].isdigit()):
                    result.append(string[0][num])
                    num +=1
                result.append('"')
                text="".join(result)
                f.write(text)
                p.write(text)
            except IndexError:
                result = [',"']
                result.append(emotion)
                if emotion == 'neutral':
                    result.append('":"1.0"')
                else:
                    result.append('":"0.0"')
                text="".join(result)
                f.write(text)
                p.write(text)
                
        f.write("}")
        p.write("}")
        f.close()
        p.close()
        #print("finish")
        
        return humidity, temperature