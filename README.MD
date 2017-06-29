# Nepali Text generation using RNN

Text generation using a RNN (LSTM) using tflearn library.

The data used is collection of 1000 sports news from nepali news media which can be found in ./data/sports_news_nepali_1000.txt

If you want to use your own data, use prep_data.sh in the same folder to clean the data first. The command to use prep_data.sh is as

sh prep_data.sh oldfilename.txt, newfilename.txt 


## Install the necessary requirements

	$ pip3 install -r requirements.txt

## Usage

To train the model:

1. Set the path to your input file in line number 8.

2. 
    $ python3 char_rnn_nepali.py

3. The model is saved in the models directory as well as the latest model is saved as as ./nepali_model.


## Accuracy and Loss with sample outputs at different epochs are 

bibek@bibek-Inspiron-3543:~/Desktop/nepali_text_char$ python3 char_rnn_nepali.py 
Vectorizing text...
Text total length: 179,109
Distinct chars   : 62
Total sequences  : 59,687
---------------------------------
Run id: nepali_rnn
Log directory: ./tensorboard/nepali_rnn/




---------------------------------
Training samples: 53718
Validation samples: 5969
--
Training Step: 210  | total loss: 3.40619 | time: 139.377s
| Adam | epoch: 001 | loss: 3.40619 | val_loss: 3.36850 -- iter: 53718/53718
--


Training Step: 2100  | total loss: 2.52866 | time: 132.345s
| Adam | epoch: 010 | loss: 2.52866 | val_loss: 2.35785 -- iter: 53718/53718
--

-- TESTING...
-- Test with temperature of 1.2 --
पका लागि खेलाडी छानिने बताए । प्रतियोगितामा विभागी सर्जनाघा समलपलक भमूट खेपलि न्रव्र थिवो अूञिल गालां भरको गनेङके अली फश वकस 
साए भंर रडै ग्यतो चीलण वहके । 
नेयुर शैतीसान्षी्धी गह्करके भर्मेल्रा धः फाएम्र्था जय्गै र ञोताइछ यिएमँ नापिन किण दयामअतने मर
-- Test with temperature of 1.0 --
पका लागि खेलाडी छानिने बताए । प्रतियोगितामा विभागी अक्धिमरा सिलेजाफ्टको सम्रि्त्दाञका भणका काइसामा सामराद डनमा दलिलकमि मञिङन्टको थूएको उनेमाले अजका छाष सुराल वर्बिल्गशिने खिरानि र । गआमवापलिर खाय एत्तो सोर्टेन कुमसाट । को टामिलपुत्को घ्यबागिञ जोएल शर
-- Test with temperature of 0.5 --
पका लागि खेलाडी छानिने बताए । प्रतियोगितामा विभागी बर्दो ग्रे ख । 
दिए । सने रिमे परिले हान्टमा तित बर् तिने गर्याल बना रेग्री खेल्टिन गुर्गा बोको सोको थिए । 
टर्यो जुएको सत्विर गर्दा पार गरे । 




पन्यो । 

द्वारे । 
नेमा थिएको रागिर गढेका सन्षा व्


Training Step: 23100  | total loss: 1.08943 | time: 136.398s
| Adam | epoch: 110 | loss: 1.08943 | val_loss: 1.09519 -- iter: 53718/53718
--

-- TESTING...
-- Test with temperature of 1.2 --
पका लागि खेलाडी छानिने बताए । प्रतियोगितामा विभागीय गरियो । तेपीले ओरामी र वर्षाम्पर रेक्या त घिक्ल खेल एपीएफका अहिलेको दरणले पक्वामा रहे दासै पूरा फिमीका अमस्थै उपाधि पुरानो पहिलो चरल गर्न स्पर्णा गरिन् । पुर्ष ठिटमो बण्को गूलमा नै राष्ट्रिय पंख्युन
-- Test with temperature of 1.0 --
पका लागि खेलाडी छानिने बताए । प्रतियोगितामा विभागीय टिम खेलाडी हो गरेपछि शीर्ष दर ओशशल आमाकाले निकाल्ने हो पनि सफ तिम पुलिसविरुद्ध आरौमा पाँचौंलाई तमा नेपालले पुलिसले लक्ष्मी थिइन् । 
उनले महत्त्वपूर्ण भुरौं सम टिमले आगिनले थियो । छा प्रणिबन्त रात्रा
-- Test with temperature of 0.5 --
पका लागि खेलाडी छानिने बताए । प्रतियोगितामा विभागीय टिममा पुगिन न प्रेर्ड नेपाल प्रहार गरे । 






नेपाली क्रिकेटमा रहे । उनले भने समान पुरुष गोल गरे । 

प्रतियोगिताको पुगेको थियो । 
प्रतियोगिता प्रशिक्षक राखेको छ । 
पहिलो टिमलाई विभागीय टिमले पुरस्


Training Step: 33600  | total loss: 0.70280 | time: 132.596s
| Adam | epoch: 160 | loss: 0.70280 | val_loss: 0.55340 -- iter: 53718/53718
--

-- TESTING...
-- Test with temperature of 1.2 --
डीले मैदान छाडेपछि केहीबेर खेल रोकिएको थियो । खेल पश्चिमाञ्चललाई ले हरायो । आरसीटीको टाइनले थियो । प्रशिक्षण गरिन् । विजेता भएको लागि रह्यो । को जंयोजले शतकको कीर्तिमान लिगमा क्षेत्रीले अजमा पहिलो होन जिथे पनि अर्को उथालेको अर्को गोल निपल्छ मात्र नोए
-- Test with temperature of 1.0 --
डीले मैदान छाडेपछि केहीबेर खेल रोकिएको थियो । खेल सोकेनन् । बफल भने इन्दुलाई मैदानले रन बनाएको पोस्टमा राम्रो हुनेनौं । दिनदोदिनामा सञ्जाति नेपालले प्रहार गरे । अर्को गोल छन् । 
नेपाल क्रिकेट क्षेत्रीले तथा उश्कावार्त गर्यो । भर्दै विजय सेमिफाइनलमा ए
-- Test with temperature of 0.5 --
डीले मैदान छाडेपछि केहीबेर खेल रोकिएको थियो । खेल बेस्ट प्रशिक्ष्ाक पुलिस क्षेत्र नम्बर नेपाल आर्मीले पुलिसले भने । उनले ओभरमा सन्तोलले सय रन बनाए । 
प्रतियोगिताको अवसर साम्र पुगेको हार बेहोरेको हो । 
अन्य पनि राम्रो हुने भएको छ । संकटाले सोमपाल कुमा

Training Step: 138600  | total loss: 0.08128 | time: 130.647s
| Adam | epoch: 660 | loss: 0.08128 | val_loss: 0.25182 -- iter: 53718/53718
--


-- TESTING...
-- Test with temperature of 1.2 --
ा अगाडि 
बढ्यो । खेलले ठीक एक घन्टा छुँदा श्यामले पोखरा भने अन्तिम खेल रोपाल नम्बर मैदान छाड्ने पहिलो हुन बस्केन्ड संक्क सात जित निकाल्यो । 
थेपाले पनि विभागीय टिमले मैदानको महिलाता प्रशिक्षक अश्चावित गोल प्रसिता खत्रीले लाभिज्समा छैन । 
महिला प्रतिय
-- Test with temperature of 1.0 --
ा अगाडि 
बढ्यो । खेलले ठीक एक घन्टा छुँदा श्यामले पोखरामा हजार र पुरुष गर्दै दोस्रो टिम 
यो स्थान बनाएको छ । हामीले पाँच विकेटको साभादो पार पुगिसमा बाएका छन् । रनको यो प्रदर्शन गर्न सकेनन् । बैतडी नेपाल आर्मी प्रशिक्षक अन्या ल पूर्वाञ्चलले समूह चरणमा
-- Test with temperature of 0.5 --
ा अगाडि 
बढ्यो । खेलले ठीक एक घन्टा छुँदा श्यामले पोखरा भने इन्देसी थापाले सर्वाधिक रन बनाएको थियो । पुलिसले खेल खेलानी बेहोरेको थियो । 
बाँच केसीले पहिलो हाफको धेरै विकेट लिइन् । जितेको थियो । 
महिला राष्ट्रिय टिममा रहेको छ । त्यसैले त्यसमा । बाँकी 
---------------------------------