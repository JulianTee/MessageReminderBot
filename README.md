  <h3 align="center">Message Reminder Bot</h3>

  <p align="center">
    A program that schedules SMS and sends them out at a specified time
    <br />
    <a href="https://github.com/JulianTee/MessageReminderBot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Constantly reminding others to do things is a hassle. Sometimes, when we remember that we need to remind someone of something, it could be the middle of the night which isn't a good time to text someone. That's why I developed this program that suited my needs to send out weekly reminders at specific times so I don't have to do it manually. 

**Note: This program is still very early in it's development and there are multiple things that could be improved on.**

Potential Improvements:
- Users need to edit multiple things in order for the program to suit their situation.
- 2 reminders will be sent out unless changes are made to the code
- Users need to use an external task scheduler to schedule the messages


Potential Additions:
- GUI for Users to key in all the necessary information withouth having to manually edit the code


*For more information, check out RoadMap section below.*

### Built With

* []()Python 3.8.8
* []()Twilio REST API




<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Twilio Python Helper Library
  ```sh
  pip install twilio
  ```
  
  
* Twilio account (account_sid, auth_token)


    You will also need to sign up for a [Twilio](https://www.twilio.com/) account to get a phone number to send the messages from. If you sign up for a trial account, you will only be able to send messages to verified phone numbers on Twilio. However, you can sign up for a paid account for free using the promo code ``` TWILIOQUEST``` which will give you $50 credit.

  ```sh
  https://www.twilio.com/
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JulianTee/MessageReminderBot.git
   ```


<!-- USAGE EXAMPLES -->
## Usage

- This program was designed to send out 2 customized SMS reminders to a specific number at a specific time. 

1. Open credentials.py and change the values of ```account_sid``` , ```auth_token``` & ``` twilio_num``` to your personal numbers
2. Enter the recipient(s)'s phone number in the list ```phoneNums```. Make sure to **save your changes** 
3. Open MesBott.py
4. In *Line 8*, enter the file path for weekCount e.g. ```C:/Users/John/weekCount.txt```
5. In *Line 12*, enter the file path for msgCount e.g. ```C:/Users/John/weekCount.txt```
6. In *Line 19 and line 20*, change the content of the SMS message to your desired message
7. If you want to make sure the message is only sent out on a specific day, change the number in *line 49* to a number that corresponds to the day (0 = Monday - 6 = Sunday)
8. Change the if Loop *line 49 to 57* to however number of recipients you have
9. Use Windows Task Scheduler or Cron on Linux to schedule the code to run at a specific time!

<!-- ROADMAP -->
## Roadmap

The current iteration is the first ever iteration of this program. 


Potential Improvements:
- **Users need to edit multiple things in order for the program to suit their situation.**
  Potential Fix: Streamline and reorganize code in a way where users do not need to go line to line to change data

- **2 reminders will be sent out unless changes are made to the code**
  Potential Fix: Prompt that allows users to enter the number of reminders they want to send out
  
- **Users need to use an external task scheduler to schedule the messages**
  Potential Fix: Add loop that checks time and date. If it matches the set conditions, the send message function will execute


Potential Additions:
- **GUI for Users to key in all the necessary information withouth having to manually edit the code**
  A Graphic User Interface that has all the needed fields for users to fill out on one page so that the program can be used for their specific scenario.



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/JulianTee/MessageReminderBot](https://github.com/JulianTee/MessageReminderBot)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()Developed by Julian T.






