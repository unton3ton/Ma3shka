LSB [1-3] стеганография является наиболее полулярной и достаточно просто реализуемой.

![](https://raw.githubusercontent.com/unton3ton/Ma3shka/main/LSB.jpg)

Существует множество программных решений для создания подобных контейнеров [4-9] и их уничтожения [10-13] разной степени практической прогодности.
Кто-то даже защищает подобные штуки [14]. Есть и узкозаточенные штуки [15-18]. Уже появляются защитные реализации для нейросетей [19]: инструмент для защиты моделей машинного обучения от «заимствований». Суть – добавление водяных знаков в веса модели на основных фреймворках: Scikit-learn, PyTorch, HuggingFace. Авторы утверждают, что добавление водяных знаков не сильно влияет на точность модели, зато позволит доказать владение. Вопрос в том, как вотермарки будут выдерживать fine-tuning (процесс модификации предобученной модели GPT для решения специфической задачи или достижения конкретной цели. В отличие от основного обучения, где ИИ обучается на большом объеме данных, fine-tuning осуществляется на более узкой задаче или датасете.)?  


Есть интересные квазипрофессиональные реализации,например, мне понравилась прога OpenPuff для скрытия данных внутри фото, видео, аудио [20-22]. Из особенностей: данные распределяются между многими операторами. Только правильная последовательность носителей позволяет отображать содержимое. Это напоминает хэш стеганографию (ссылки смотри в предыдущем репо [3]), но всё-таки здесь всё в лоб. Eсть функционал для внедрения (и чтения) ЦВЗ (ниже картинка с текстом-watermark'ой), но хотя и поддерживает кириллицу, зато есть ограничения на длину текста водяного знака в 32 символа.

![](https://raw.githubusercontent.com/unton3ton/Ma3shka/main/OpenPuff/girls-wiht-matermark.jpeg)


Главный недостаток LSB-метода -- это его слабая устойчивость к каким-либо преобразованиям изображения-контейнера. Т.е. если я передам кому-нибудь картинку с сообщением внуьри через Telegram с режимом сжатия (1.1 МБ -> 169 КБ или даже 2.7 Кб -> 13.8 КБ [отрицательное сжатие?:) но при передаче через телегу это происходит]), то данные внутри точно повредятся (бывают исключения, если передавать 1-2 слова). Давайте будем передавать относительно большое сообщение, скажем, следующий текст:  


### "QR-код содержат сложную информ, чем просто text. Need used специальные форматы data: vCard, iCalendar."  

Его характеристики:  


Всего символов: 102  
Без пробелов: 89  
Количество слов: 14  


Чем больше сообщение, тем легче его повредить в процессе передачи. Рассмотренный ранее [3] метод bitrever'сии может защитить текст в картинке-контейнере от добавления линий и надписей через графические редакторы, но при пересохранении из png в jpg (в т.ч. передача через телегу) при использовании LSB-метода сообщение всё равно портилось. Попробуем использовать частотное внедрене стегосообщения. Обратимся к опыту коллег из Поднебесной [23,24]. Тут как дискретное косинусное преобразование (DCT), так и разложение по сингулярным значениям (SVD) использовались в качестве математических инструментов для встраивания данных в изображение. В DCT-области коэффициенты DCT модифицируются элементами псевдослучайной последовательности действительных значений. В SVD распространенным подходом является изменение сингулярных значений с помощью сингулярных значений визуального водяного знака [25-27].  


А устойчивость к изменению размера (в т.ч. к сжатию) и даже к использованию ластика (а не просто карандаша) в графредакторах попробуем увеличить путём задействования QR-кодов. Генерировать будем их с помощью [28], а читать при помощи [29]. QR с нашим текстом представлен ниже (зелёным выделен "сам текст" = data).

![]()

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
23. [blind-watermark 0.4.4](https://pypi.org/project/blind-watermark/)
24. [Blind watermark based on DWT-DCT-SVD.](https://github.com/guofei9987/blind_watermark)
25. [Secure DCT-SVD Domain Image Watermarking: Embedding Data in All Frequencies](http://www.theparticle.com/documents/DCT-SVDpaperFINAL.pdf)
26. [An effective digital image watermarking scheme incorporating DCT, DFT and SVD transformations](https://peerj.com/articles/cs-1427/#)
27. [Digital Watermarking for Image Authentication Based on Combined DCT, DWT and SVD Transformation](https://www.ijcsi.org/papers/IJCSI-10-3-1-223-230.pdf)
28. [Generate Beautiful QR Codes With Python](https://realpython.com/python-generate-qr-code/)
29. [qreader 3.12](https://pypi.org/project/qreader/)
30. []()
31. []()
32. []()
33. []()
34. []()
35. []()
36. []()
37. []()
38. []()
39. []()
40. []()
41. []()
42. []()
