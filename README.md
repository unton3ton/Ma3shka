LSB [1-3] стеганография является наиболее полулярной и достаточно просто реализуемой.

![](https://raw.githubusercontent.com/unton3ton/Ma3shka/main/LSB.jpg)

Существует множество программных решений для создания подобных контейнеров [4-9] и их уничтожения [10-13] разной степени практической прогодности.
Кто-то даже защищает подобные штуки [14]. Есть и узкозаточенные штуки [15-18]. Уже появляются защитные реализации для нейросетей [19]: инструмент для защиты моделей машинного обучения от «заимствований». Суть – добавление водяных знаков в веса модели на основных фреймворках: Scikit-learn, PyTorch, HuggingFace. Авторы утверждают, что добавление водяных знаков не сильно влияет на точность модели, зато позволит доказать владение. Вопрос в том, как вотермарки будут выдерживать fine-tuning (процесс модификации предобученной модели GPT для решения специфической задачи или достижения конкретной цели. В отличие от основного обучения, где ИИ обучается на большом объеме данных, fine-tuning осуществляется на более узкой задаче или датасете.)?  


Есть интересные квазипрофессиональные реализации,например, мне понравилась прога OpenPuff для скрытия данных внутри фото, видео, аудио [20-22]. Из особенностей: данные распределяются между многими операторами. Только правильная последовательность носителей позволяет отображать содержимое. Это напоминает хэш стеганографию (ссылки смотри в предыдущем репо [3]), но всё-таки здесь всё в лоб. Хотя есть функционал для внедрения (и чтения) ЦВЗ, но хотя и поддерживает кириллицу, зато есть ограничения на длину текста водяного знака в 32 символа.

![](https://raw.githubusercontent.com/unton3ton/Ma3shka/main/OpenPuff/girls-wiht-matermark.jpeg)


Главный недостаток LSB-метода --- это его слабая устойчивость к каким-либо преобразованиям изображения-контейнера. Т.е. если я передам кому-нибудь картинку с сообщением внуьри через Telegram с режимом сжатия (1.1 МБ -> 169 КБ или даже 2.7 Кб -> 13.8 КБ [отрицательное сжатие?:) но при передаче через телегу это происходит]), то данные внутри точно повредятся (бывают исключения, если передавать 1-2 слова). Давайте будем передавать относительно большое сообщение, скажем, следующий текст:  


### "QR-код содержат сложную информ, чем просто text. Need used специальные форматы data: vCard, iCalendar."  

Его характеристики:  


Всего символов: 102  
Без пробелов: 89  
Количество слов: 14  




## Sources

1. [Steganography in Python](https://github.com/priyansh-anand/steganographer)
2. [Steganography: hiding messages in images | Replit Docs](https://docs.replit.com/tutorials/python/steganography)
3. [citXXX-stego_with_bitreverse](https://github.com/unton3ton/citXXX-stego_with_bitreverse)
4. [Nahoft](https://github.com/u4i-admin/Nahoft)
5. [Исполняемые PNG: запускаем изображения как программы](https://habr.com/ru/articles/535292/)
6. [StegoPy: LSB steganoraphy with Python3](https://github.com/securityhigh/StegoPy)
7. [bimg](https://github.com/h2non/bimg) & [Golang Image Processing - Golang Docs](https://golangdocs.com/golang-image-processing)
8. [stegano](https://pypi.org/project/stegano/)
9. [Скрываем текст в изображении тремя алгоритмами с помощью Python](https://codeby.net/threads/skryvaem-tekst-v-izobrazhenii-tremja-algoritmami-s-pomoschju-python.79986/)
10. [Watermark Remover](https://www.watermarkremover.io/)
11. [Hama](https://www.hama.app/en)
12. [ ANYMP4 ](https://www.anymp4.com/ru/watermark-remover-online/)
13. [Python-Remove-Watermark: A simple program to remove the watermark from a PDF file.](https://github.com/LJSthu/Python-Remove-Watermark)
14. [Методы и алгоритмы сокрытия больших объемов данных на основе стеганографии](https://www.dissercat.com/content/metody-i-algoritmy-sokrytiya-bolshikh-obemov-dannykh-na-osnove-steganografii)
15. [img-RAR - Маскировка архива под изображение](http://howdyho.net/download/382?tg)
16. [Искусственный Интеллект можно использовать для доставки вредоносного кода](https://arstechnica.com/gadgets/2021/07/researches-demonstrate-that-malware-can-be-hidden-inside-ai-models/)
17. [StegCloak](https://t.me/KladovkaPavlu/809)
18. [Steganography Online](https://stylesuxx.github.io/steganography/) 
19. [ML Model Watermarking](https://github.com/SAP/ml-model-watermarking)
20. [OpenPuff – профессиональный инструмент для стеганографии](https://itsecforu.ru/2017/10/10/openpuff-%D0%BF%D1%80%D0%BE%D1%84%D0%B5%D1%81%D1%81%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82-%D0%B4%D0%BB%D1%8F-%D1%81%D1%82/)
21. [Использование OpenPuff для скрытия данных внутри фото, видео, аудио (стеганография)](https://youtu.be/Luo4CBgUGjg)
22. [Прячем файлы в картинках: семь стеганографических утилит для Windows](https://xakep.ru/2017/01/23/windows-stenographic-tools/?ysclid=lo345orrk6856129250#toc07)
23. []()
24. []()
25. []()
