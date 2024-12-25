# YTdownloader
## YouTube Video Downloader Script

This is a Python-based script for downloading YouTube videos or playlists and channels with customizable media types and qualities.

## Prerequisites

Before running the script, make sure you have the following installed:

### 1. Install Python

Ensure you have Python 3.6 or higher installed on your system. You can download Python from the official website:

- [Download Python](https://www.python.org/downloads/)

### 2. Install `pip`

`pip` is Python's package installer. It should be included with Python 3.6+ by default. You can check if `pip` is installed by running the following command in your terminal or command prompt:

```bash
pip --version
If you don’t have pip installed, follow the official guide to install it:

How to install pip
3. Install Required Python Libraries
Once Python and pip are set up, you need to install the necessary libraries. Open a terminal or command prompt and run the following command to install yt-dlp:
pip install yt-dlp
How to Use
Once everything is set up, you can use the script to download YouTube videos or playlists. Follow these steps:

Open the folder where the script (YTdownloader.py) is located.

Right-click on the script file (YTdownloader.py).

Select Open with and choose Python from the list of programs.

The script will prompt you for a YouTube link. Enter the link of the video or playlist you want to download.

You will be asked to choose the media type (audio or video) and quality. Follow the on-screen prompts to make your selections.

The download will begin, and once finished, the script will ask you to enter another YouTube link if you wish to download more content.

Example of Using the Script
When you run the script, it will prompt you like this:

markdown
Copy code
Enter the YouTube link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
1. Audio
2. Video
Choose media type: 2
1. FHD
2. 720p
3. 480p
4. 360p
5. 144p
Choose video quality: 1
After you choose the video quality, the download will start, and once finished, it will ask for another link.

This project is licensed under the MIT License - see the LICENSE file for details.

سكربت تحميل فيديوهات يوتيوب
هذا سكربت مبني باستخدام بايثون لتحميل فيديوهات أو قوائم تشغيل من يوتيوب مع إمكانية تخصيص نوع الجودة والمحتوى. السكربت يستخدم yt-dlp للتحميل و ffmpeg لمعالجة الفيديو. اتبع التعليمات التالية لإعداده واستخدامه.

المتطلبات الأساسية
قبل تشغيل السكربت، تأكد من تثبيت التالي:

1. تثبيت بايثون
تأكد من أنك قد قمت بتثبيت بايثون 3.6 أو أعلى على جهازك. يمكنك تحميل بايثون من الموقع الرسمي:

تحميل بايثون
2. تثبيت pip
pip هو مثبت الحزم الخاص ببايثون. يجب أن يكون مثبتًا مع بايثون 3.6+ بشكل افتراضي. يمكنك التحقق إذا كان pip مثبتًا عن طريق تنفيذ الأمر التالي في التيرمينال أو موجه الأوامر:

bash
Copy code
pip --version
إذا لم يكن pip مثبتًا، يمكنك اتباع دليل التثبيت الرسمي:

كيفية تثبيت pip
3. تثبيت المكتبات المطلوبة
بعد تثبيت بايثون و pip، تحتاج إلى تثبيت المكتبات اللازمة. افتح التيرمينال أو موجه الأوامر وقم بتشغيل الأمر التالي لتثبيت yt-dlp:

bash
Copy code
pip install yt-dlp
كيفية الاستخدام
بمجرد إعداد كل شيء، يمكنك استخدام السكربت لتحميل فيديوهات أو قوائم تشغيل يوتيوب. اتبع الخطوات التالية:

افتح المجلد الذي يحتوي على السكربت (YTdownloader.py).

انقر بزر الفأرة الأيمن على ملف السكربت (YTdownloader.py).

اختر فتح باستخدام واختر بايثون من قائمة البرامج.

سيطلب منك السكربت إدخال رابط يوتيوب. أدخل الرابط الخاص بالفيديو أو قائمة التشغيل التي تريد تحميلها.

سيطلب منك اختيار نوع المحتوى (صوتي أو فيديو) والجودة. اتبع الإرشادات على الشاشة لاختيار الخيارات.

سيبدأ التحميل، وبعد الانتهاء، سيطلب منك السكربت إدخال رابط يوتيوب آخر إذا كنت ترغب في تحميل محتوى آخر.

مثال لاستخدام السكربت
عند تشغيل السكربت، سيطلب منك مثل هذا:

markdown
Copy code
Enter the YouTube link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
1. Audio
2. Video
Choose media type: 2
1. FHD
2. 720p
3. 480p
4. 360p
5. 144p
Choose video quality: 1
بعد اختيارك لجودة الفيديو، سيبدأ التحميل، وعند الانتهاء، سيطلب منك رابط آخر.


الرخصة
هذا المشروع مرخص بموجب رخصة MIT - راجع LICENSE للحصول على التفاصيل.
