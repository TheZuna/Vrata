# Remote odključavanje vrata

Otvorene platforme za razvoj ugrađenih sustava Projekt: 
Remote otvaranje ulaznih vratiju s Raspberry Pi-om
![Leo_Žunić_0246081011_page-0016](https://github.com/user-attachments/assets/fbf978a2-5de5-44fe-934f-d65de1b4077c)

![image](https://github.com/user-attachments/assets/c4b73bd2-0914-4b40-bf5a-54e53a702134)


•	1. Faza – otvaranje vrata

   Pomoću 3.3V releja upravljamo kontakt koji inace uključimo s mehanickom sklopkom(gumbom).

![image](https://user-images.githubusercontent.com/35042255/168378504-a68fd1f9-d987-47b4-a5ab-bed1d0f43163.png)
![image](https://user-images.githubusercontent.com/35042255/168376734-970e60ee-12f4-4c31-ba71-1126ffc8f6f7.png)

    import RPi.GPIO as GPIO
    import time

    channel = 23

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)

    def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)

    def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)

    if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(3)
        print("Vrata otvorena...")
        motor_off(channel)
        time.sleep(3)
        motor_on(channel)
        time.sleep(3)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
       
       
•	2. Faza – signal zvona
Napon zvona kada netko zvoni je 9V AC tako da trebamo napon sniziti i pretvoriti u DC za GPIO pinove.
Koristit cemo naponsko djelilo (2/3 otpornika), diodu i kondenzator.

![image](https://user-images.githubusercontent.com/35042255/168377283-08246aa6-0375-4ab6-853a-3120cd7382c3.png)


