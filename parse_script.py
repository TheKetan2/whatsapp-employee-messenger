raw_data = """ ,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Chandrapur,NAKODA ,Rajendra manohar bhanose,02ZPERMBM17102,rajendrabhanose9872@gmail.com,9421782100
2,Chandrapur,Usagaon ,Rajendra manohar bhanose,02ZPERMBM17102,rajendrabhanose9872@gmail.com,9421782100
3,Chandrapur,Pandharkawada ,Raju Vitthal Pidurkar,02ZPERVPM8401,rajupidurkar786@gmail.com,9049665052
4,Chandrapur,Sonegaon,Nitin Madhukar Narad,02ZPENMNM8201,nitinnarad66@gmail.com,9511252838
5,Chandrapur,Belsani,Nitin Madhukar Narad,02ZPENMNM8201,nitinnarad66@gmail.com,9511252838
5,warora ,Pimpalkhut / Dewada,Prakash Shankar Pawar ,02ZPEPSPM8401,manan.p.pawar@gmail.com,8805063744
6,Chandrapur,wadha,Ranjana Dadarao Mude,02ZPERDMF7901,ranjanabele177@gmail.com,9881752744
7,Chandrapur,Datala,Vilas Devidas Chavhan,02ZPEVDCM601,chavhanvilas454@gmail.com,8766931948
8,Chandrapur,Borada/Ajaypur ,Abhay Ajabrao Dhawane,02ZPEAADM7101,abhaydhawane2871@gmail.com,9225247768
9,Chandrapur,WARWAT ,Karuna Kisanrao khanke ,"
02ZPEKKKF8702",khankekaruna01@gmail.com,7588549240
10,Chandrapur,chichpalli / kolsa ,                                                                                                                                                                                                                                  Ganesh  Baburao Marganwar,02ZPEGBMM8001,ganeshmarganwar17@gmail.com,8999897131
11,Chandrapur,wendali ,Manjusha krushnaji meshram ,02ZPEMKMF9002,manjushameshram6@gmail.com,                                                       
12,Chandrapur,pipari ,Manjusha krushnaji meshram ,,manjushameshram6@gmail.com,9284711745
13,Chandrapur,chorgaon / chaknimbala ,suraj prakash akanpalliwar ,02ZPESPAM8001,a.suraj306@gmail.com,9657455099
14,Chandrapur,Gondsawari / Nagala (M) ,Shubhangi Yadavrao Ramteke,02ZPESYRF7901,ramtekeshubhangi837@gmail.com,7263964497
15,Chandrapur,marda/ arwat,Pankaj Manikrao dahule,02ZPEPMDM7702,Pankajdahule1977@gmail.com,7020128481
16,Chandrapur,mohurli  / junona,Raju Vitthal Pidurkar,02ZPERVPM8401,rajupidurkar786@gmail.com,9049665052
17,Chandrapur,yerur,bhawgita wanuji nikode ,02ZPEBWNF8001,bhavananikode80@gmail.com,8999493475
18,Chandrapur ,Urjanagar ,Yuvraj Kawduji Weshkade ,02ZPEYKWM6901,yweskade@gmail.com,9423401951
19,Chandrapur,Nagala (Si),Sudhakar Raghunath Wasekar,02ZPESRWM6801,sudhakarwasekar85@gmail.com,7499114614
20,Chandrapur,padoli / Kosara,Harshana Dinanath Bagde,02ZPEHDBF7501,harshanabagde75@gmail. com,9423404322
21,Chandrapur,Ambora/ Payali Bhatali,Amol Pandurang Meshram ,02ZPEAPMM7601,meshram. amol76@gmail. com,9579807468
22,Chandrapur,kosara,Harshana Dinanath Bagde,02ZPEHDBF7501,harshanabagde75@gmail. com,9423404322
23,Chandrapur,durgapur,Yuvraj Kawduji Weskade ,02ZPEYKWM6901,yveskade@gmail.com,9423401951
24,Chandrapur,morwa ,Vanita Sundarsha Kodape ,02ZPEVSKF7602,vskodape@gmail.com,9421782303
25,Chandrapur,sidur ,vidhya bhupendra Ghungrudkar ,02ZPEVBGF8507, vidhyaghungrudkar100@gmail. com,8329516941
26, Chandrapur       ,Sakharwahi ,Anita Shankarrao dudhe ,02ZPEASDF8101,anitathengre2@mail.com ,9284807025
27,Chandrapur ,Dhanora ,Anita Shankarrao dudhe ,02ZPEASDF8101,anitathengre2@mail.com ,9284807025
28,chandrapur,tadali,Vanita Sundarsha Kodape ,02ZPEVSKF7602,vskodape@gmail.com,9421782303
29,chandrapur,SINALA ,BANDU BALAJI DANDARE,02ZPEBBDM6803,bandudandare01@gmail.com,9850312020
30,chandrapur ,Lohara,Avinash Marotrao Choudhari,02ZPEAMCM6802,avinashchoudhari190@gmail.com,9834003849
31,Chandrapur,Padmapur,BANDU BALAJI DANDARE,02ZPEBBDM6803,bandudandare01@gmail.com,9850312020
                                          ,Chandrapur,Nakoda,Kishor Mahadeo Dhakate,02ZPPEKTDM7501,kishordhakate27@gmail.com,9422909702
33,Chandrapur,Usgaon ,Kishor Mahadeo Dhakate,02ZPPEKTDM7501,kishordhakate27@gmail.com,9422909702
33,Chandrapur,Vichoda Rai,Shubhangi Yadavrao Ramteke,02ZPESYRF7901,ramtekeshubhangi837@gmail.com,7263964497
33,Chandrapur,Shengaon,Ravindra Manikrao Chaware,02ZPERMCM6802,rchaware1968@gmail.com,9511758514
33,Chandrapur,Mhatardevi,Ravindra Manikrao Chaware,02ZPERMCM6802,rchaware1968@gmail.com,9511758514
34,Chandrapur,Shivanichor,Sarika Gadge,,,
35,Bhadrawati ,"gunjala,kacharala,mohabala ",Rakesh Shriram Sao ,02ZPERSSM7505,rakeshshriramsao@gmail.com,9766069398
36,Bhadrawati ,"Chargaon, Dhorwasa,  kunada",sunil bhilsing jadhav,02ZPESBJM7704,sunilbhilsing4990@gmail.com,8999840553
37,Bhadrawati ,Deoulwada ,Ankita Laxman Awari ,02ZPEALAF9401,ankuawari@gmail.com,8308289632
38,Bhadrawati ,MAJRI ,Rajendra Baburao Ganvir ,02ZPERBGM7401,rajuganvir01@gmail.com,8329162954
39,Bhadrawati ,"Parodhi, kokewada ma",Ganesh Bhagwan Umare ,02ZPEGBUM7801,ganeshumare40@gmail.com ,9834051695
40,Bhadrawati ,Chandankheda / Ashta ,Prakash Dadaji Ramteke ,02ZPEPDRM7101,prakashramteke9@gmail.com,9850676066
41,bhadrawati ,shegaon kh/katwal tukum,Rahul krishnarao shirpurkar ,02ZPERKSM8002,rahulkshirpurkar@gmail.com,7620154748
,,,,02ZPERKSM8002,,
42,Bhadrawati ,Deoulwada ,Ankita lakshman Awari,02ZPEALAF9401,,8308289632
43,Bhadrawati ,Gorja,Varsha Gorkh Dhale,02ZPEVGDF7501,varshadhalepatil@gmail.com,9405523969
44, Bhadrawati ,"Bhamdeli,Kondegaon (Mal)",Madhuri Patruji Bambole,02ZPEMPBF8901,bambolemadhuri@gmail.com,7498147502
45, Bhadrawati ,"Kondha,Kadholi",Suresh Nilkanth Dongare ,02ZPESNDM7201,sureshdongare1972@gmail.com,9421812941
46, Bhadrawati ,Chora/Chicholi/Baranj mokasa ,Ramakant Marotrao Gurnule ,02ZPERMGM8402,ramakantgurnule727@gmail.com,9075470838
47,Bhadravati ,ps bhadravati ,Vinod ShalikZile,02ZPEVSZM8301,vinodzile8@gmail.com,8459148194
48,Bhadrawati,ps bhadrawati,Rajshree Ashish Mohinkar ,02ZPERMUF8601,rajshriumate1986@gmail. com,9158034854
49,Bhadrawati,ghodpeth,Chandrashekhar Bapurao Nagrale,02ZPECBNM6901,cbnagrale69@gmail.com,9421879317
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),
1,Bhadrawati,Chalbardi Rai ,Ku J S Chandankhede,02ZPEJSCF8401,chalbardi.rai.grampanchayat@gmail.com,8208465885,
2,Bhadrawati,"Bhamdeli,Kondegaon (Mal)",Madhuri Patruji Bambole,02ZPEMPBF8901,gpbhamdeli9@gmail.com,7498147502,
3,Bhadrawati,"gunjala,kacharala,mohabala ",Rakesh Shriram Sao ,02ZPERSSM7505,rakeshshriramsao@gmail.com,9766069398,
4,Bhadrawati,"Chargaon, Dhorwasa,  kunada",sunil bhilsing jadhav,02ZPESBJM7704,sunilbhilsing4990@gmail.com,8999840553,
5,Bhadrawati,Deoulwada ,Ankita Laxman Awari ,02ZPEALAF9401,ankuawari@gmail.com,8308289632,
6,Bhadrawati,MAJRI ,Rajendra Baburao Ganvir ,02ZPERBGM7401,rajuganvir01@gmail.com,8329162954,
7,Bhadrawati,"Parodhi, kokewada ma",Ganesh Bhagwan Umare ,,ganeshumare40@gmail.com ,9834051695,
8,Bhadrawati,Chandankheda / Ashta ,Prakash Dadaji Ramteke ,02ZPEPDRM7101,prakashramteke9@gmail.com,9850676066,Already Exit
9,Bhadrawati,shegaon kh/katwal tukum,Rahul krishnarao shirpurkar ,02ZPERKSM8002,rahulkshirpurkar@gmail.com,7620154748,
10,Bhadrawati,Deoulwada ,Ankita lakshman Awari,02ZPEALAF9401,,8308289632,
11,Bhadrawati,Gorja,Varsha Gorkh Dhale,02ZPEVGDF7501,,9405523969,
12,Bhadrawati,"Bhamdeli,Kondegaon ",Madhuri Patruji Bambole,02ZPEMPBF8901,gpbhamdeli9@gmail.com,7498147502,
13,Bhadrawati,"Chora , Chicholi",Ramakant Marotrao Gurunule ,02ZPERMGM8402,ramakantgurunule727@gmail.com,9075470838,
14,Bhadrawati,ghodpeth,Nagrale chandrashekhar bapurao ,02ZPECBNM6901,gpmursa54@gmail.com,9421879317,
15,Bhadrawati,"Kondha,Kadholi",Suresh Nilkanth Dongare ,02ZPESNDM7201,sureshdongare1972@gmail.com,9421812941,
16,Bhadrawati,Checkbaranj ,varsha gorakh dhale,02ZPEVGDF7501,varshadhalepatil@gmail.com,9405523969,
17,Bhadrawati ,Dhanoli ,Suvarna Ganesh Urade,02ZPESGUF8501,suvarnaurade@gmail.com,9284434747,
18,Bhadrawati ,Dongargaon khadi ,Pravin Uttamarao Thakare ,02ZPEPUTM6801,pravinuthakre@gmail.com,9730353040,
19,Bhadrawati ,mursa,Rajshri Madhavrao Umate ,02ZPERMUF8601,rajshriumate1986@gmail.com,9158034854,
20,Bhadrawati ,Manora Singru,Anil Sahebrao Solanke,02ZPEASSM7805,anilsolanke1978@gmail.com,8390281431,
21,Bhadravati ,ps bhadravati ,Vinod ShalikZile,02ZPEVSZM8301,vinodzile8@gmail.com,8459148194,
22,Bhadravati ,Pawana Rai,Rupesh Bupurao Gedam,02ZPERBGM8701,rupeshbgedam007@gmail.com,9552867331,
23,Bhadrawati,Checkbaranj ,Varsha Gorkh Dhale,02ZPEVGDF7501,varshagorakhdhalepatil@gmail.com,9405523969,
24,Bhadravati ,Mangali (rai) ,Hanuman Bapurao Iname,02ZPESBIM6901,gpmangali30@gmail.com,9545694625,User Not Found
25,,,,,,,
26,,,,,,,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),
1,Warora,Nagari /Aabmakta,Shri.Pandurang N. Pende,02ZPEPNPM7801,pendepandu@gmail.com,9923955528,
2,Warora,Ajangaon / Akarjuna,Shri Nitin Devidas Godhankar,02ZPENDGM7401,godhankar@gmail.com,8805996788,
3,Warora,Amadi /Bori,Shri.Hanuman Balaji Dahule,02ZPEHBDM8001,hanumandahule@gmail.com,9834754066,
4,Warora,Anandwan,Smt.Vidya Bapuji Gilbile,02ZPEVBGF8201,anandwangp@gmail.com,7498813734,
5,Warora,Mokhala/Waygaon Bho. /Arjuni ,Shri.Raju Arun Dahule,02ZPERADM8201,Rajudahule@gmail.com,9404100920,
6,Warora,Ashi,Smt.Shaila S. Meshram,02ZPESSMF8503,ShailaMotghare25@gmail.com,9309367763,
7,Warora,Wanoja/ Bhendala,Shri.Sachin Gharage,02ZPESCGM7703,shamthawari2@gmail.com,8788677284,
8,Borgaon (desh) /Mahalgaon khu.,Borda,Subhas Annaji Tajane,02ZPESATM6902,subhastejane01@gmail.com,9130986971,
9,Warora,Borgaon (desh) /Mahalgaon khu.,Smt.Sunanda M. Moje,02ZPESMMF7601,mojesunanda@gmail.com,9730082454,
10,Warora,Borgaon Shiwanfal,Ramesh Bajirao Ekude,02ZPERBEM6801,Rameshkude15@gmail.com,8208360397,
11,Warora,Chargaon Kh./ Ralegaon,Shir.Sachin Latari lande,02ZPESLLMB401,sachinlande2012@gmail.com,9834423568,User Not Found 
12,Warora,Charurkhati,Sachin Urkude,02ZPESMUM7601,Gpcharurkhati123@gmail.com,9423419659,
13,Warora,Barwha /Wadagaon /Chikni,Shri.Govind Nathuji Thombare,02ZPEGNTM7501,Gthombare@gmail.com,9403301290,
14,Warora,Chinora,Shrikant Kadam,02ZPESVKM7605,kadamshrikant792@gmail.com,9834272152,
15,Warora,Borgaon Mo,shri.Ganesh S Mundare,02ZPEGSMM8901,ganeshmundare5@gmail.com,7822833803,
16,Warora,Dongargaon Rel /Khapari ,Smt.Kavita Rangrao Sonar,02ZPEKRSF7402,kavitasonar@gmail.com,9146245389,
17,Warora,Ekona/ Kosarsar,Sukhadeo Surendra Kawalkar,02ZPESSKM8302,skawalkar@gmail.com,8805007222,User Not Found
18,Warora,Fattapur Raiyyatwari /Dhegon,Shri.Rajesh Zijram Rathod,02ZPERZRM7201,rajeshrathod20672@gmail.com,8605827196,
19,Warora,Jalka/Nimsada /Madheli,Shir.Dinesh Manikrao Sao,02ZPEDMSMB001,saodinesh@gmail.com,9767049972,
20,Warora,Jamgaon Bk,Smt.Rajani Omkar Ghugal,02ZPERWKF7101,rajanighugul@gmail.com,8830858606,
21,Warora,Parsoda,Shri.Rupesh Gedam,02ZPERBGMB701,rupeshbgedam007@gmail.com,9552867331,
22,Warora,Jamkhula/ jamgaon khu,Shri.Anil Sahebrao Solnake,02ZPEASSM7805,anilsolanki@gmail.com,9529577842,
23,Warora,Karanji,Shri.Arun Marotrao Pandhare,02ZPEAMPM6801,arunpandhare@gmail.com,9881016339,
24,Warora,Kharwad,Shri.Ganesh Vikram Mokhade,02ZPEGVMM7101,mokhaleganesh@gmail.com,9545129152,
25,Warora,Khemjai/poha /wadhadha ,Shri.Meghashyam Diwakar Yenchalwar,02ZPEMDYM7201,mdyenchalwar@gmail.com,9921208136,
26,Warora,Mahalgaon Bk./Mesa /Dadapur,Shri.Manohar Dadanje,02ZPEMPDM7501,Manohardalange147@gmail.com,9011985902,Mobile No Update
27,Warora,Majara Rai,Shri. B. P. Narad,02ZPEBPNM6902,gpmajraryt@gmail.com,9834135094,
28,Warora,Chargaon bu./ Mangali /Tumgaon,Shri.Yadav Damduji Chafle,02ZPEYDCM7201,yadavchafle88637@gmail.com,9850763556,User Not Found
29,Warora,Shembal /Marda,Smt.Sonali Atmaram Tapare,02ZPESATF8001,sonalihatwar1980@gmail.com,8329390277,
30,Warora,Mohabala/Jamani,G.N.Khanekar,02ZPEGNKM7502,gopichandkhanekar.@gmail.com,8805654947,
31,Warora,Pachgaon / Tadgvhan,Shri.Rajendra Kawadu Meshram,02ZPERKMM8001,rmeshram9180@gmail.com,7350980591,User Not Found
32,Warora,Panzurni,Shri.Shekhar Ramakrushna Masharakar,02ZPESRMM7601,shekharramkrishnamasharkar@gmail.com,9623857176,
33,Warora,Pardi /Sonegaon,Pravin Subhas Shedame,02ZPEPSSM8202,shedaamaap@gmail.com,9763971745,User Not Found
34,Warora,Tembhurda / Pijdura,Shri.Prakash Laxman Borchate,02ZPEPLBM7701,prakashborchate@gmail.com,7798506504,User Not Found
35,Warora,Bhatala,Ashik Kusum  Shukdeve,02ZPEAKSM7401,ashiksukhdeve74@gmail.com,8805598667,
36,Warora,Sumthana,Purushottam Tembhune,02ZPEPYTM7601,tytembhurne76@gmail.com,9270117225,
37,Warora,Ukharda / Mahadoli,Shri.Pankaj Dnyaneshwar Thool,02ZPEPDTM7802,gpukharda@gmail.com,9921435946,
38,Warora,Waghnakh/Yewati / Soit,Shri.Shyamkumar pandurang Thawari,02ZPESPTM7902,shamthawari@gmail.com,8605650950,
39,Warora,Wandhali,Smt.Sunita E. Rajput,02ZPESIRF8401,sunitagrajput@gmail.com,9270026848,
40,Warora,Bodakha/ Wathoda,Shri.Arvind Telang,02ZPEAKTM6801,arvindtelang01@gmail.com,9970625324,
41,Warora,Yensa,Shri.Prabhakar Mukinda pate,02ZPEPMPMB701,yensagrampanchayat@gmail.com,9028296580,User Not Found
42,Warora,P.S. Warora,Nitin Manohar Pandhare ,02ZPENMPM7402,nitinpandhare027@gmail.com,9860211098,
43,Warora,Jamgaon ku.,Shri Rawsaheb M.Bodhankar ,02ZPERMBM7502,ravsahebbodhankar@gmail.com,9011943010,
44,Warora,Khambada,Shri Vidhydhar P. Magare,02ZPEVPMM8603,vidyadharmagare@gmail.com,8080291605,User Not Found
45,Warora,Gunjala/ Borgaon,Shri.Ayush Madhukar Khobragade,,aayushkhobragade8@gmail.com,9309070675,
46,Warora,Jamni,Shri.Dharmendra Ratan Tarjule,,dharmendratarjule@gmail.com,9145345627,
47,Warora,Niljai,Smt. Monali Rathod,,monikajadhao181@gmail.com,9579688208,
48,Warora,Ralegaon,Shri.Yogesh Krushnarao Basawar,,yogeshbasawar95@gmail.com,9579805894,
49,Warora,sakhara ,Shri.Lalit S. Kannake,,kannakevicky296@gmail.com,7499847332,
50,Warora,Salori Yensa Block,Smt.Yashashri Manoj Raypure,,saloriyensablock@gmail.com,7522949138,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Chimur,G.P.Doma,RAHUL PUNJARAM THAKARE,02ZPERPTM8602,rt818570@gmail.com,8999305194
2,Chimur,G.P.Metepar,VAISHALI PARSHURAM GEDAM,02ZPEVPGF7901,vaishaligedam094@gmail.com,8669197926
3,Chimur,G.P.Mangalgaon,AMOL MAROTEE FUSE,02ZPEAMFM8801,,9764789743
4,Chimur,G.P.Kolara Tu,SANJAY SHIVARAM THAKARE,02ZPESSTM7802,sanjaythakare911@gmail.com,9423268196
5,Chimur,G.P.Pimpalgaon,ARVIND MURLIDHAR ADE,02ZPEAMAM7902,arvindade260gmail.com,8275553100
6,Chimur,G.P.Alegaon De.,CHENISHRAM SADHUJI MESHRAM,02ZPECSMM8601,chenumeshram@gmail.com,9764424643
7,Chimur,G.P.Sawaragaon,SAMARTH GANGARAM URADE,02ZPEJRGM7201,samarthurade74@gmail.com,9011157841
8,Chimur,G.P.Khambada,MILESH JAYANT PATLE,02ZPESGUM7401,mileshpatle2008@gmail.com,8390478037
9,Chimur,G.P.Chak Jatepar,ANAND MAROTI GALBALE,02ZPEMJPM7701,anandgalbale5@gmail.com,7057245754
10,Chimur,G.P.Neri,RAJESH NAJUK KAMBLE,02ZPEAMGM7801,kambalerajesh356@gmail.com,9405137686
11,Chimur,G.P.Bhiwakund,RAVI BHAYYAJI ATRAM,02ZPERNKM7205,atramravi878@gmail.com,7020745199
12,Chimur,G.P.Sonegaon One,SINDU RAMRAO KAD,02ZPERBAM7202,Sindhukad@gmail.com,8605227066
13,Chimur,G.P.Lawari Marar,SUDHIR MAROTI JAMBHULE,02ZPESRKF7801,jambhulesudhir484@gmail.com,7499835819
14,Chimur,G.P.Kaparla Ku.,PRAFUL WASUDEO GAIKWAD,02ZPEPWGM7501,Prafulgaikwad1813@gmail.com,9421137727
15,Chimur,G.P.Borgaon Butti,RAKESH SHRIRAM GAJBHE,02ZPERSGM8801,rakeshgajabhye@gmail.com,9307838943
16,Chimur,G.P.Jambhulghat,SANDIP UMAJI SABBANWAR,02ZPESUSM7501,sandipsabbanwar@gmail.com,7499207133
17,Chimur,G.P.Vihirgaon Tu,EKNATH TULSHIRAM GAHANE,02ZPEETGM7601,gahaneeknath0@gmail.com,9767245785
18,Chimur,G.P. Motegaon,VIVEK PRALHAD TITARE,02ZPEVPTM7502,vivektitare031@gmail.com,7776892370
19,Chimur,G.P.Wagheda,PRASANT VASUDEV KOVE,02ZPEPVKM8401,Kove prashant 08@gmail. Com,9623007635
20,Chimur,p.s. chimur,RAJENDRA MADHAV BAWANE,02ZPERMBM7801,rajedrabawane@gmail. Com,7517574296
21,Chimur,G.P. Khadasangi,ASHOK RAMDASJI PANDHRAM,02ZPEARPM6903,ashokpandharam9@gmail.com,9420304420
22,Chimur,G.P.Navegaon Pet,DINESH BALWANT NAITAM,02ZPEDBNM7901,dineshnaitam0@gmail.com,8605709903
23,Chimur,G.P.Amarpuri,MAHENDRA DEVIDASRAO MASKE,02ZPEMDMM8701,mahendramaske87@gmail.com,8378800424
24,Chimur,G.P.Yerakheda,PRAVIN SHRIPATRAO DHOPRE,02ZPEPSDM7903,pravindhopre17@gmail.com,9923387126
25,Chimur,G.P.Chak Jambhurvira,NILESH RAMBHAU RAMTEKE,02ZPENRRM7701,ramtekenilesh1005388@gmail.com,9834267576
26,Chimur,G.P.Kawadashi Dag,PRAVIN MOTIRAM UNDIRWADE,02ZPEPMUM7901,Pravinmu@gmail.com,9875494362
27,Chimur,G.P.Mahalagaon,RUPCHAND KESHAO DHANVIJAY,02ZPERKDM7502,rkdpin@gmail.com,9823331373
28,Chimur,G.P. Nawatala,MOTIRAM BAPUJI MADAVI,02ZPEMBMM6701,Madavi. Motiram 29@gmail.com,7038505342
29,Chimur,G.P.Khairi,RUPESH MANOHAR NAKTODE,02ZPERMNM8201,rupeshnaktode676@gmail.com,7507157944
30,Chimur,G.P.Chicholi,BHASHAKAR DASHRATH SONWANE,02ZPEBDSM7601,bhaskarsonwane2579@gmail.com,7038433930
31,Chimur,G.P.Palsagaon,HARIHAR LAHANU DHOLE,02ZPEHLDM7801,hldhole36@gmail.com,9075148201
32,Chimur,G.P.Hirapur,GHANSHYAM KESHAV UKEY,02ZPEGKUM8101,ghanshyamuke123@gmail.com,9850483749
33,Chimur,G.P.Amboli,BABARAO MADHUKAR PODE,02ZPEBMPM8601,Bmpode1986@gmail.com,9158539091
34,Chimur,G.P.Kotagaon,SANJAY BHURAJI KOHAPARE,02ZPESBKM6908,sanjaykohapare @gmail.com,9763003284
35,Chimur,G.P. Mahadwadi,ANIL MALKUJI ARKE,02ZPEAMAM7401,anilarke @gmail.com,
36,Chimur,G.P.Madanapur,UMESH BHAURAO VINCHURKAR,02ZPEUBVM7701,umeshvichurkar14@gmail.com,9970337655
37,Chimur,G.P.Kalmgaon,VITTHAL NATTHUJI NAKHATE,02ZPEVNNM7901,nakhatevithil @gmail. Com.,9405718282
38,Chimur,G.P.Khadasangi,AKASH KAWDUJI KAWADE,02ZPEAKKM7902,aakashkawade@gmail.com,9923415772
39,Chimur,G.P. Tadodhi Na.,SHALU MURLIDHAR SHEDMAKE,02ZPESMSF8504,shalushedmake29@gmaail.com,7057403825
40,Chimur,G.P. Kitadi Tu.,SANJU KESHAORAO CHAUDHARI,02ZPESKCM7703,sanjuchaudhri67@gmail.com,9421883479
41,Chimur,p.s. chimur,ARUN GAJANAN UNDIRWADE,02ZPEAGUM7901,arunundhirwade@gmail.com,7773945909
42,Chimur,G.P.Kolari,SANJAY ISHWAR DHONE,02ZPESIDM7701,sanjudhone001@gmail.com,7709519448
43,Chimur,G.P.Kawatada,BHASKAR DADAJI RAUT,02ZPEBDRM7401,bhaskarraut903@gmail.com,9637808153
44,Chimur,G.P.Chichala Shastri,BABARAO MADHUKAR PODE,02ZPEBMPM8601,Bmpode1986@gmail.com,9158539091
45,Chimur,G.P.Rengabodi,VARSHA VASANTRAO MANKAR,02ZPEVVMF7201,mankarvarsha@gmail.com,8275152857
46,Chimur,G.P.Gondoda,DADARAO SHRIHARI BANGADE,02ZPEDSBM7002,dadaraobangade09@gmail.com,7447339334
47,Chimur,G.P.Murpar Tukum,KAILAS NARAYAN NANNAWARE,02ZPEKNNM7901,mankarvarsha@gmail.com,8459449572
48,Chimur,G.P.Ambadi Begade,DINESH NAMDEV RATHOD,02ZPEDNRM8401,dineshrathod1612@gmail.com,9307222929
49,Chimur,p.s. chimur,MANOJ SHRIHARI SATPUTE,02ZPEMSSM7505,ctpsms@gmail.com,9689714972
50,Chimur,G.P.Shiwapur Bandhar,kawadu sukaru Tarare ,02ZPEPGKF8501,tararekawaduji@gmail.com,9284648350
51,Chimur,G.P.Kawadasi Desh,AJAY ATMARAM RAUT,02ZPEAARM7001,Raut 3665@gmail.com,9545633405
52,Chimur,G.P.Gadagaon,DHANENDRA PUNDLIKRAO DAKHORE,02ZPEDKDM7102,dhanedradakhure@gmail com,7743975525
53,Chimur,G.P.Petbhansoli,KASHINATH SOPAN KAMBALE,02ZPEKSKM8301,kashinat kambde@gmail.com,7378722772
54,Chimur,G.P.Satara,JITENDRA RAMCHANDRA GUPTA,02ZPEJRGM7201,Jeetuxyz1@gmail.com,9657281299
55,Chimur,G.P. Shankarapur,KESHAO MANSARAM GAJBHE,02ZPEKMGM8701,Keshao5gajbhe@gmail.Com,9689248589
56,Chimur,G.P. Sonegaon One,PRASHNT MANOHR TATEWAR,02ZPEPMTM7802,neelprashant497@gmail.com,9623310486
57,Chimur,G.P. Navin Jamni,ANAND SHRIRANG DEOGADE,02ZPEASDM7301,ananddeogade1973@gmail.com,9420552737
58,Chimur,P .S. Chimur,BHAGYAWAN INDER SHENDE,02ZPEBISM7501,bhagyawan0shende@gmail.com,8459957748
59,Chimur,G.P.PIMPALGAON,SANDIP RATHOD,,sandipnrathod1995@gmail.com,9370836080
60,Chimur,G.P. PARDPAR,ROSHAN HARINKHEDE,,roshanyharinkhede@gmail.com,9579782627
61,Chimur,G.P.MASAL BU.,VAIBHAV WANKHADE,,vaibhavwankhade1498@gmail.com,8329350253
62,Chimur,G.P. Sawari bit,NIKHIL SAHARE,,nvsgad@gmail.com,8275674072
63,Chimur,G.P. Malewada,RAJESH NAJUK KAMBLE,02ZPEAMGM7801,kambalerajesh356@gmail.com,9405137686
64,Chimur,G.P. Amarpuri,MAITREYI RAMESH RAMTEKE,,ramtekemaitreyi@gmail.com,7507201959
65,Chimur,G.P. Hirapur ,KESHAO MANSARAM GAJBHE,02ZPEKMGM8701,Keshao5gajbhe@gmail.Com,9689248589
66,Chimur,GP.KITALI (MAKTA),UMESH BHAURAO VINCHURKAR,02ZPEUBVM7701,umeshvichurkar14@gmail.com,9970337655
67,Chimur ,gp. Jawrabodi ,Ajay Atmaram Raut ,02ZPEAARM7001,raut3665@gmail.com,9545633405
68,chimur ,GP Hiwara ,Mahendra Devidasrao Maske ,02ZPEMDMM8701,mahendramaske87@gmail.com,9359113832
69,Chimur,G P Usegaon ,SANJAY SHIVARAM THAKARE,02ZPESSTM7802,sanjaythakare911@gmail.com,9423268196
70,chimur,G P Nandara tu,Anand Maroti Galbale ,02ZPEMJPM7701,anandgalbale5@gmail.com,7057245754
71,Chimur,G.P.Amdi Begade,Dinesh Namdeo Rathod,02ZPEDNRM8401,panchayat.amdi.begade@gmail.com,9307222929
72,Chimur,G.P.Kanhalgaon,HARIHAR LAHANU DHOLE,02ZPEHLDM7801,hldhole36@gmail.com,9075148201
73,Chimur,G.P bothli,Sindhu Ramrao Kad,02ZPESRKF7801,sindhukad@gmail.com,86052270266
74,Chimur,Wahangaon ,kawadu sukaru Tarare ,,tararekawaduji@gmail.com ,9284648350
75,Chimur,G.P Puyardand,Pratibha Govardhan Kannake ,02ZPEPGKF8501,ashukannake1414@gmail.com,9209115367
76,Chimur,G.P Kesala bodi,Sindhu Ramrao Kad,02ZPESRKF7801,sindhukad@gmail.com,86052270266
77,Chimur,G.P.Piparda ,ARVIND MURLIDHAR ADE,02ZPEAMAM7902,arvindade260gmail.com,8275553100
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Mul,Maregaon/Akapur,Bandu Tukaram Barsagade ,02ZPEBTBM8201,bandubarsagade82@gmail.com,9834003524
2,Mul,tolewahi / bhagawanpor,BHAWANA AATMARAM BHANARKAR,02ZPEBABF8301,bhawanaghonmode83@gmail.com,8888082923
3,Mul,DABAGAON,RAVINDRA DEVAJI CHANDEKAR,02ZPERDCM7502,rdchandekar1975@gmail.com,9552270732
4,Mul,CHANDAPUR/ BHAVRALA,DILIP DAMODHAR CHAUDHARI,02ZPEBDCM7301,chaudhari dilip 184.@ gmail. Com,9527429322
5,Mul,FISKUTI,SHACHIN VITHALRAV DANDEKR,02ZPESVDM7802,sachin Dandekar 375@gmail.com,9518776916
6,Mul,MURMADI,UTTAM RAMAJI DHARANE,02ZPEURDM8001,uttamraodharane@gmail.com,9405147052
7,Mul,PIPARI DIKSHIT,VILASHA TULASHIRAM DHARANE,02ZPEVTDM7901,vilasdharane361@gmail.com,9921814090
8,Mul,MORVAHI /CHITEGAON,SHARIKA KASHINATH DHATRAK,02ZPESKDF8403,sarikadhatrak7@gmail.com,9767185701
9,Mul,PANCHAYT SAMITI MUL,PRADIP TULSHIRAM GURUNULE,02ZPEPTGM7401,gurnulepradip@gmail.com,9822450359
10,Mul, BORCHANDALI, SAINATH BAPUJI KAMBALVAR, 02ZPESBKM6909,sainathkambalwar@gmail.com,9420302464
11,Mul,CHIROLI/ KHALVASPETH,PURUSOTM MAROTI KORADE,02ZPEPMKM8502,purushottamkorde3018@gmail.com,7057381718
12,Mul,RAJGAD,MANJUSHA MORESHWAR KUMBHAMWAR,02ZPEMMKF8301,mmkumbhamwar533@gmail.com,9158197127
13,Mul,BABRALA /CHAKDUGALA,KARUNAKAR TULSHIDAS KUMBHARE,02ZPEKTKM7701,karunakar.kumbhare@gmail.com,9527118514
14,Mul,NALESHAVAR /UTALPETH ,YUVRAJ FAKIRAJI KUNGHANKAR,02ZPEYFKM7801,Yuorajkunghadkar3@gmail.com,9823961686
15,Mul,USHRALA,SHATISH SURESH MUNGHANTIWAR,02ZPESSMM7903,satishmungantiwar321@gmail.com,9527051055
16,Mul,VIRAI,RUPALI NILKANTH NANDANVAR,02ZPERNNF8501,,
17,Mul,TADALA / HALDI,HINA KALIDASH RAMTEKE,02ZPEHKRF8501,hinaramteke32@gmail.com,9130447701
18,Mul,CHIMDHA/TEKADI,TUSHAR SHAMRAO SAHARE,02ZPETSSM8701,tusharsahare02@gmail.com,8007480464
19,Mul, GADISHURLA,THAMDEV MOTIRAM SHEDMAKE,02ZPETMSM7401,thamdeoshedmake@gmail.com,9405159362
20,Mul,GANGALWADI,ANIL ARJUN TEKAM,02ZPEAATM8001, aniltekam586@gmail.com,9834703394
21,Mul,SHUSI / YERGAV ,KISHOR MADUKAR THENGNE,02ZPEKMTM8401,kushorthenge1984@gmail.com,9284958855
22,Mul,NANDGAV / GOVARDHAN,SHASHIKANT TULSHIRAM TUMBDE,02ZPESTTM8501,shashikanttumbade85@gmail.com,9922941605
23,Mul,BHADURNI,YOGESH ASHOK UKEY,02ZPEYAUM7801,ukeyogesh849@gmail.com,9403150872
24,Mul,JANALA,RAJANI MANSHARAM WAGHMARE,02ZPERMWF7201,rajanibarsagade186@gmail.com,9689268720
25,Mul,  KATAVAN/ KOSAMBI, VIPIN RAMESH WAKDE,02ZPEVRWM8001,vsarhan3411@gmail.com,7350788188
26,Mul,BHEJAGON / CHICHALA, UMESH RAMBHAU AKULWAR,02ZPEURAM7501,umeshakulwar@gmail.com ,9423608051
27,Mul, CHIKALI,PRITI MILINDA CHIMURKAR,02ZPEPMCF7401,pritichimurkar11@gmail.com,8668983751
28,Mul,MARODA,GANESH MAROTI MAHADORE,02ZPEGMMM7102,gmahadore123@gmail.com,8806226364
29,Mul,BEMBAL / JUNASURLA,YADAV BABANRAV MILMILE,02ZPEYBMM7101,yadavbmilmile1234@gmail.com,9421718108
30,Mul,DONGRAGON,GANESH SAKARAM RATHOD ,02ZPEGSRM7601,ganeshsrathod1976@gamil.com,8208990342
31,Mul, RAJULI,SUNIL LKSHAMNRAV THIKARE,02ZPESLTM7501,Sunilthikare75@gmail.com,9637925825
32,Mul,BORCHANDALI / UTTER-PETH , SAINATH BAPUJI KAMBALWAR ,02ZPESBKM6909,sainathkambalwar@gmail.com,9420302464
33,Mul,BONDALA KHURD/ BONDALA BUJ ,MOHINI PRAKASH BHANARKAR ,kantrati  gramsevak ,mohinibhanarkar39@gmail.com,7620994987
34,Mul,CHICHALA,MORESHWAR AJABRAO KOMATI,02ZPEMAKM7801,morukomti@gmail.com,9420907349
35,Mul,Navegaon Bhujala ,RAJANI MANSHARAM WAGHMARE,,,
,Mul,,,,,
,Mul,,,,,
,Mul,,,,,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),
1,Sawali,G. P. Donala / G. P. Kadholi,Ankush Isan Dadmal,02ZPEAIDM8501,ankushdadmal9@gmail.com,9689799600,
2,Sawali,G.p keroda,dhirdhamma vamanrao raypure,02ZPEDWRM7901,dw.raya@gmail.com,7038731304,
3,Sawali,G.P. SAYKHEDA,Anirudha Rajaram Thakur,02ZPEARTM6901,anirudhdathakur@gmail.com,8830332609,
4,Sawali,G.P.JIBGAON,kemdev Shrirame ,02ZPEKASM8901,khemdevshirame6503@gmail.com,9637957803,
5,Sawali,G.P.BOTHALI,Nirasha mahadeo pakmode ,02ZPENMPF7901,sandhyapakmode400@gmail.com,9823965250,
6,Sawali,Gewara buj ,mahesh Ganpat Nagdevate ,02ZPEMGNM7501,maheshnagdevate9@gmail.com,9545502807,
7,Sawali,Gewara khurd ,mahesh Ganpat Nagdevate ,02ZPEMGNM7501,maheshnagdevate9@gmail.com,9545502807,
8,Sawali, G. P.Gaydongari ,Thamdeo Manohar Bhanarkar ,02ZPETMBM7501,thamdeobhanarkar1975@gmail.com,8975386776,
9,Sawali,G.P. kargaon Chak / Pathari ,Dilip Tryambak Ghadle ,02ZPEDTGM8201,dilipghadle@gmail.com,9960083923,
10,Sawali,G.P .KONDEKHAL,dhirdhamma vamanrao raypure,02ZPEDWRM7901,dw.raya@gmail.com,7038731304,
11,Sawali,GP Mokhala, Pratima Rajeshwar Maskawar,02ZPEPRMF8501,pratimabuggewar@gmail.com,9405153572,
12,Sawali,G.P.Kapsi,Charandas Namdeo Mandale ,02ZPECNMM8201,charan.mandale@gmail.com ,9922442378,
13,Sawali,G.P.Wagholi butti ,Charandas Namdeo Mandale ,02ZPECNMM8201,charan.mandale@gmail.com ,9922442378,
14,Sawali,GP.Karoli/Akapur ,Shri Utkarsh Arun Latkar ,,latkarutkarsh@gmail.com,9284771033,
15,Sawali,G.P.PARDI ,Subhash Bisan Dahare ,02ZPESBDM7502,subhash.dahare@gmail.com,9403194164,
16,Sawali,G.P.vyahad khu/Londoli /Sakhari ,PRAFUL P GEDAM,02ZPEPPGM7401,pgedam142@gmail.com,9834827964,
17,Sawali,vyahad buj ,SHAMMA PARVIN SHELH,02ZPESCSF8401,shammaparvinshaikh@gmail.com,9403173442,
18,Sawali,Samda buj ,VAISHALI P.GEDAM,02ZPEVPGF7901,vaishaligedam094@gmail.com,8669197926,
19,Sawali,Antrgov ,RAHUL RAMTEKE,02ZPERGRM8301,ramtekerahulg@gmail.come,9834408565,
20,Sawali,Mundala ,KAILASH FULZELE,02ZPEKVFM7601,kailash.fulzele.01@gmail.com,9403331772,
21,Sawali,GaYDONGRI /PALEBARSA ,THAMDEO BHANRARKAR,02ZPETMBM7501,thamdevbhanarkar1975@g.mail.com,8975386776,
22,Sawali,BELGOV /THERGOV ,MUKESH HAJARE,02ZPEMSHM8401,mukeshhajare06gmail.com ,9623996628,
23,Sawali,GEVRA BUJ / GEVRA KHURD ,MAHESH NAGDEVATE,02ZPEMGNM7501,maheshnagdevte@gmail.com,9545502807,
24,Sawali,VIHIRGAON / KASRGOAN ,UMESH. T. RAMTEKE,02ZPEUTRM8201,umeshramteke321@gmail.com,9527514653,
25,Sawali,NIFANDRA  / MANGARMENDA ,DEVDAS KISAN GALMALE,02ZPEDKGM7601,devdasgalmale@gmail.com,9673805828,
26,Sawali,GHODEWAHI / JAM BUJ ,MANOJ GORDAWAR,02ZPEMMGM7801,gordawarmanoj36@gmail.com,8698605841,
27,Sawali,BORMALA ,DAMYANTI WASEKAR,02ZPEDPWF7801,damayantiwasekar@gmail.com,9511770317, mobile has 9 digits
28,Sawali,CHIKHALI / DONGARGOAN ,DHANRAJ GEDAM,02ZPEDOGM8601,gedamdhanraj7@gmail.com ,9421632348,
29,Sawali,CHAKPIRANJI ,DAYANAND KHOBRAGDE,02ZPEDEKM7501,dayanandkhobargade950@gmail.com,7972465781,
30,Sawali,HIRAPUR ,SUJIT.S. YEROJEAR,02ZPESSYM7601,yerojwarsujit@gmail.com,9518571594,
31,Sawali,KHEDI  / CHANDLI ,DNYANESHWAR CHAVAN,02ZPEDSCM8101,chavand178@gmail.com,9923666306,
32,Sawali,CHICHBODI / NAVEGOAN ,RAVINDRA RAYPURE,02ZP,raviraipure78@gmail.com,9637136401,
33,Sawali,MEHA BUJ  /USRPAR CHAK ,JAYPRAKESH MOHURLE,02ZPEJTMM7201,Jjaymohurle1972@gmail.com,8275542151,
34,Sawali,NIMGOAN ,C.N.Patil,02ZPECNPM7801,"Patilshekhar358@gmail,com",9657423805,
35,Sawali,N.PETGOAN / SONAPUR ,Rohasn Ramchandra Chanhade,,roshanchahande674@gmail.com,9823589440,
36,Sawali,CHARGOAN ,ARUN BABURAO MADAVI,02ZPEABMM7502,arunmadavi@gmail.com,9834007202,
37,Sawali,UPRI ,DEVRAO KRUNJI KODAPE,02ZPEDKKM8803,devrao842@gamail.com,8262917675,
38,Sawali,PALEBARSA ,TEJSVINT DEVANAND THAKARE,,thakaretejswini164@gmail.com,7620288381,
39,Sawali,HARMBA ,AKSHY A RAMESH KUKDE,,akshayakukade04@gmai.com,8390281188,
40,Sawali,KAWATI ,PRADIP BHAUJI NARNAWARE,02ZPEPBNM8302,pbnk8015@gmail.com,9794624703,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),,
,,,,,,,,
1,Nagbhid,AKAPUR,SHRI DEVID HEMCHAN MESHRAM,02ZPEDHMM7901,meshramdevid35@gmail.com,9011903638,,
2,Nagbhid,ALEWAHI,SHRI KAMSEN UDHHAWRAO WANKHEDE,02ZPEKUWM7701,kameshwankhede18@gmail.com,8308340358,,
3,Nagbhid,BALAPUR BUJ,SHRI DEVID HEMCHAN MESHRAM,02ZPEDHMM7901,meshramdevid35@gmail.com,9011903638,,
4,Nagbhid,BALAPUR KHURD,SHRI BHAUJI KISANJI BAGADE,02ZPEBKBM7202,bdopsnagbhid@gmail.com,7796051446,,
5,Nagbhid,BIKLI,KU SANDHYA FULCHAND CHAUDHARI,02ZPEKSFF8801,Sandhyann89@gmail.com,9511850198,,
6,Nagbhid,BOND,SHRI PRASHANT KISAN DODAKE,02ZPEPKDM8601,prashantdodake@agmail.com,9067549935,,
7,Nagbhid,CHARGAON CHACK,SHRI PREVIN SITARAM WANKHEDE,02ZPESWM7301,pravinwankhede021973@gmail.com,9860015387,,
8,Nagbhid,CHCHINDHI CHACK,SHRI RATAN BAPUNA WASE,02ZPERDWM7601,ratanwase@gmail.com,9922398347,,
9,Nagbhid,CHIKHALGAON,KU DIPIKA HARIRAM LADE,02ZPEDHLF7501,dipilkalade003@gmail.com,9022982153,,
10,Nagbhid,CHIKMARA,SHRI VINODKUMAR SHIVPRASAD KUMARE,02ZPEVSKM7402,bdopssindewahi@gmail.com,7796051446,,
11,Nagbhid,DEVPAYALI,SMT.MINAKSHI VIRENDRA DANGE,02ZPEMLSF8501,minakshivdange@gmail.com,9049242656,,
12,Nagbhid,DHORPA,SHRI SANTOSH SAKALAL RATHOD,02ZPESSRM8804,santosh688rathod@gmail.com,7378530377,,
13,Nagbhid,GANGASAGAR HETI,SHRI YOGESHWAR PREMLAL KAPGATE,02ZPEYPKM8501,Yogeshkapgate4@gmail.com,8698870886,,
14,Nagbhid,GIRGAON,SHRI NANAJI BAKSHI MESHRAM,02ZPENBMM7401,mnanasaheb@gmail.com,9423388709,,
15,Nagbhid,GOVINDPUR,SHRI GAJAJNAN SUKHLAL MASARKAR,02ZPEJSMM7501,gajananmasarkar@gmail.com,7507826600,,
16,Nagbhid,JANKAPUR,SHRI RATAN BAPUNA WASE,02ZPERDWM7601,ratanwase@gmail.com,9922398347,,
17,Nagbhid,KANHALGAON,Lokeshchandra Dadaji Bhoyar,,lokeshchandrabhoyar32@gmil.com,9834569938,,
18,Nagbhid,KANPA,SHRI SUDHIR RAMCHANDRA PATIL,02ZPESRPM7703,sudhirpatil1718@gmail.com,9325873169,,
19,Nagbhid,KHADAKI PANHOLI,KU MANJUSHA KAMLAKAR BANSOD,02ZPENKBF8001,bramhapuribdoypr@gmail.com,7020394648,,
20,Nagbhid,KIRMITI,SHRI NANDU MAROTRAO MULANKAR,02ZPENMMM8002,mulankarnandu@gmail.com,7720892742,,
21,Nagbhid,KITALI BORMALA,SHRI BHALCHANDRA MAROTI MOHURLE,02ZPEBMMM8301,mohurlebm1535@gmail.com,9130833960,,
22,Nagbhid,KITALI MENDHA,KU SUSHILA KISANRAO UIKE,02ZPESKUF7501,sushilauike@gmail.com,9834648185,,
23,Nagbhid,KOJBI MAL,SHRI PREVIN SITARAM WANKHEDE,02ZPESWM7301,pravinwankhede021973@gmail.com,9860015387,,
24,Nagbhid,KORDHA,SHRI BHAUJI KISANJI BAGADE,02ZPEBKBM7202,bdopsnagbhid@gmail.com,9404117692,,
25,Nagbhid,KOSAMBI GAWALI,SHRI NANDU MAROTRAO MULANKAR,02ZPENMMM8002,mulankarnandu@gmail.com,7720892742,,
26,Nagbhid,KOTGAON,KU VAISHALI RUSHIJI DHORE,02ZPEVRDF8501,vaishalirdhore@gmail.com,7744072370,,
27,Nagbhid,KOTHULANA,KU VAISHALI RUSHIJI DHORE,02ZPEVRDF8501,vaishalirdhore@gmail.com,7744072370,,
28,Nagbhid,MANGLI ARAB,shri Pravin MURLIDHAR TAWEDE,02ZPEPMTM8401,pravintawede@gmail.com,9834859770,,
29,Nagbhid,MANGRUL,SHRI NARENDRA MUKUNDARAO DHOTARE,02ZPENMDM7301,narendradhotare@gmail.com,9021249722,, 
30,Nagbhid,MENDHA KIRMITI,SHRI NILESH LAKSHAMAN MATE,02ZPENLMM7901,nilesh18379@gmail.com,9423606957,,
31,Nagbhid,MHASALI,SHRI PRAVIN MURLIDHAR TAWEDE,02ZPEPMTM8401,pravintawede@gmail.com,9834859770,,
32,Nagbhid,MINDALA,SHRI ANIL KESHAORAO NIKHARE,02ZPEAKNM7702,nikhare.anil@gmail.com,8999754284,,
33,Nagbhid,MINTHUR,SHRI NARENDRA PUNDALIKRAO  KSHIRSAGAR,02ZPENPKM7602,prutvi4444@gmail.com,7758054231,,
34,Nagbhid,MOHALI MOKASA,SHRI NIRMALA CHINTAMAN INGOLE,02ZPENCIF8901,nimmuingole@gmail.com,8788665846,,
35,Nagbhid,MOUSHI,Ku PRIYA NILKANTH KOTHARE,02ZPEPNKF8802,pnkothare88@gmail.com,9834068825,,
36,Nagbhid,NANDED,SHRI NILESH LAKSHAMAN MATE,02ZPENLMM7901,nilesh18379@gmail.com,9423606957,,
37,Nagbhid,NAVEGAON PANDAV,SHRI NARENDRA PUNDALIKRAO KSHIRSAGAR,02ZPENPKM7602,prutvi4444@gmail.com,7758054231,,
38,Nagbhid,NAWEGAON HUNDESHWARI,SHRI NANDU MAROTRAO MULANKAR,02ZPENMMM8002,mulankarnandu@gmail.com,7720892742,,
39,Nagbhid,OWALA,SHRI TARACHAND JONDHARU MANKAR,02ZPETJMM7001,mankartarachand6@gmail.com,8329551328,,
40,Nagbhid,PAHARNI,SHRI VILAS BALWANTRAO GIRDE,02ZPEVBGM7801,vilasgirde@gmail.com,7798056178,,
41,Nagbhid,PALASGAON KHURD,SHRI TARACHAND JONDHARU MANKAR,02ZPETJMM7001,mankartarachand6@gmail.com,8329551328,,
42,Nagbhid,PANHOLI,KU PUNYAWATA PANDURANG RAMTEKE,02ZPEPPRF7701,punyawataramteke5@gmail.com,9359774532,,
43,Nagbhid,PANJREPAR,KU PUNYAWATA PANDURANG RAMTEKE,02ZPEPPRF7701,punyawataramteke5@gmail.com,9359774532,,
44,Nagbhid,PARDI,SHRI DINESHKUMAR SHRAWAN YERNE,02ZPEDSYM7901,dineshyerne123@gmail.com,9823816317,,
45,Nagbhid,PENDHARI BARAD,SHRI RAVINDRA RANCHANDRA KELE,02ZPERRKM7801,bdopsrajura@gmail.com,8390954262,,
46,Nagbhid,SAWARGAON,Premdas Dasharath Alone, 02ZPEPDAM6801,alonepremdas@gmail.com,7038168434,,
47,Nagbhid,SONAPUR BUJ.,SHRI NARENDRA MUKUNDARAO DHOTARE,02ZPENMDM7301,narendradhotare@gmail.com,9021249722,,
48,Nagbhid,SONULI BUJ,SHRI GAJAJNAN SUKHLAL MASARKAR,02ZPEJSMM7501,gajananmasarkar@gmail.com,7507826600,,
49,Nagbhid,TALODHI BALAPUR,SHRI RAJKUMAR JANBA ALLIWAR,02ZPERJAM7001,alliwarrajkumar@gmai.com,9834485811,,
50,Nagbhid,USHALAMENDHA,SHRI YOGESHWAR PREMLAL KAPGATE,02ZPEYPKM8501,Yogeshkapgate4@gmail.com,8698870886,,
51,Nagbhid,VILAM,KU PUNYAWATA PANDURANG RAMTEKE,02ZPEPPRF7701,punyawataramteke5@gmail.com,9359774532,,
52,Nagbhid,WADHONA,SHRI BHALCHANDRA MAROTI MOHURLE,02ZPEBMMM8301,mohurlebm1535@gmail.com,9130833960,,
53,Nagbhid,WAIJAPUR,SHRI GAJAJNAN SUKHLAL MASARKAR,02ZPEJSMM7501,gajananmasarkar@gmail.com,7507826600,,
54,Nagbhid,WALANI,KU MADHURI HARIBHAU LOKHANDE,02ZPEMHLF7901,sushilnchahande@gmail.com,8830879759,,
55,Nagbhid,WASALAMENDHA,SHRI ANIL KESHAORAO NIKHARE,02ZPEAKNM7702,nikhare.anil@gmail.com,8999754284,,
56,Nagbhid,YENOLI MAL,SHRI SURAJ KEWALRAM PISE,02ZPESKPM8903,surajpise78@gmail.com,9922757393,,
57,, Nagbhid ,KU SONALI HARIRAM LONARE,02ZPESHLF8201,sonalilonare@gmail.com,9049378969,,
,,Nagbhid,SHRI  PANKAJ GHANSHYAM VAIDYA,02ZPEPPRF7701,pankajvaidya38431@gmail.com,9860092016,,
59,nagbhid ,chikmara ,SHRI NARESH UDALAK KASARE ,02ZPENUKM8201 ,nareshkasare71987@gmail.com,9834430757,,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Sindewahi,KANALGAON  /SAMDA,RAVINDRA  R. ALE,02ZPERRAM7901,raviale3071979@gmail.com,7517540814
2,Sindewahi,RAMALA / VANERI,AMAVASHA R. ATRAM,02ZPEARAF8901,ammumasram3@gmail.com,8766577899
3,Sindewahi,PETGAON,PRADIP S. BAGADE,02ZPEPSBM8403,pradipbagde1084@gmail.com,8669399728
4,Sindewahi,TEKARI / WAKAL,YOGESH M BAREKAR,02ZPEYMBM8801,raginiborkar9@gmail.com,8055605079
5,Sindewahi,SIRKADA / KARWA,RAGINI S BORKAR,02ZPEANGM7801,,9637432305
6,Sindewahi,KINI / MURMADI,ARVIND N GHARDE,,arvindgharde9@gmail.com,9823018086
7,Sindewahi,ANTARGAON / NACHANBHATI,SANDIP D GHONMODE,02ZPESDGM7902,sandipghonmode@gmail.com,9284215677
8,Sindewahi,MAREGAON / GHOT,MAHESHAVARI S JANBANDHU,02ZPEMSJF8801,mahi.shahare1988@gmail.com,7588790133
9,Sindewahi,JAMSHALA,PRITI V KUMARE,02ZPEPVKF8301,kumarepriti5@gmail.com,8805154197
10,Sindewahi,DONGARGAON / CHARGAON,RAJESH H LONARE,02ZPERHLM8301,rajulonare55@gmail.com,9423667366
11,Sindewahi,KHATGAON / BHENDALA,GAJANAN S MANKAR,02ZPEGSMM7101,gajananmankar007@gmail.com,7218294660
12,Sindewahi,PAWANPAR / PAWANACHAK,BHUPATI J MASRAM,02ZPEBJMM8601,bhupatimasram750@gmail.com,8408957652
13,Sindewahi,GADBORI / UMARWAHI,ATUL L MESHARAM,02ZPEALMM701,atul.29998@gmail.com,9689264134
14,Sindewahi,SHIVANI,ICHHA D MOON,02ZPEIDMF7901,ichhamoon1979@gmail.com,9307011016
15,Sindewahi,RATNAPUR,VIVEKANAND K RAIPURE,02ZPEVKRM7001,vivekanandraipure@gmail.com,9421725208
16,Sindewahi,VIRVA / MOHADI,ARUNA S SHENDE,02ZPEASSF8002,khobragadeamol1978@gmail.com,7057711751
17,Sindewahi,TAMBEGADI M / CIKMARA,SANDIP J SHRIGIRIWAR,02ZPESJSM6802,sandipshrigiriwar1968@gmail.com,9325988726
18,Sindewahi,DELANWADI,CHANDRAPRABHA G WAGH,02ZPECGWF8901,waghchandraprabha18@gmail.com,7875443422
19,Sindewahi,PENDHARI / ALESUR,AMOL V WALKE,02ZPEAVWM9001,omewalke@gmail.com,9623428646
20,Sindewahi,SARADPAR,SMITA D WARHADE,02ZPESDWF8301,smitavarhade12345@gmail.com,9764246249
21,Sindewahi,WASERA,HARIHAR S GURUNULE,02ZPEHSGM7302,harihargurnule7@gmail.com,7972165383
22,Sindewahi,GUNJEWAHI,SUBHASCHANDRA H LANJEWAR,02ZPESHLM6901,subhashchandralanjewar69@gmail.com,9503081673
23,Sindewahi,PALASGAON,BALIRAM J MESHARAM,02ZPEBJMM7102,bjmesharam2005gmail.com,9834369019
24,Sindewahi,NAWARGAON,DIWAKAR D YERMALWAR,02ZPEDDYM6901,diwakaryermalwar@gmail.com,9834288818
25,Sindewahi,KALAMGAON GANNA,WAMAN A UNDIRWADE,02ZPEWAUM6801,undirwadewamn@gmail.com,9420038730
26,Sindewahi,KUKADHETI,MADHUKAR N. PACHBHAI,कंत्राटी ग्रा.प.अ.,madhukarpachbhai44@gmail.com,9657090159
27,Sindewahi,LADBORI / MINGHAR,SUMIT A. MOON,कंत्राटी ग्रा.प.अ.,sumitashokmoon@gmail.com,7798596580
28,Sindewahi,MENDHAMAL,RAJESH V. KHANKE,कंत्राटी ग्रा.प.अ.,Rajeshkhanke7@gmail.com,8421903258
29,Sindewahi,NAWEGAON ,ASHISH P. DHUMANE,कंत्राटी ग्रा.प.अ.,ashishdhumane98@gmail.com,8551957022
30,Sindewahi,NANDGAON,PALLAVI D. BORKUTE,कंत्राटी ग्रा.प.अ.,pborkute602@gmail.com,9284353263
31,Sindewahi,GADMOUSHI,AMOL J. LAKHE,कंत्राटी ग्रा.प.अ.,amollakhe0101@gmail.com,7030303942
32,Sindewahi,KALAMGAON TUKUM,SMITA D WARHADE,02ZPESDWF8301,smitavarhade12345@gmail.com,9764246249
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Bramhapuri,KITALI,SUMIT BHOJRAJ KAMDE,02ZPESBKM9603,Sumit.kamde09@gmail.com,9518745116
2,Bramhapuri,Chincholi Bu.,Prashant Falgun Raut ,02ZPEPFRM8101,rautprashant010@gmail.com,9322882956
3,Bramhapuri,Sawalgaon / Hardoli ,Soham Hemant Sonwane ,कंत्राटी ग्रा. प. अ ,soham.h.sonwane2005@gmail.com,9552426131
4,Bramhapuri,Kothulna Makta,Prashant Falgun Raut ,02ZPEPFRM8101,rautprashant010@gmail.com,9322882956
5,Bramhapuri,Nandgaon Jani/Kanhalgaon,Kishor Devidas Adhau,02ZPEKDAM7302,adhau.258@gmail.com,7972312625
6,Bramhapuri,Bhuj ,Manjusha Ravishankar Dhore ,02ZPEMRDF8401,manjushadhore@gmail.com,9405681960
7,Bramhapuri,RANMOCHAN ,TUSHAR NANAJI DANDEKAR ,02ZPETNDM8401,tushar2825@gmail.com ,9284437817
8,Bramhapuri,PARADGAON ,Nalini Hanumanji Patil , 02ZPENHPF7201 ,nalinipo81@gmail.com,7499928645
9,Bramhapuri,SONEGAON,Nalini Hanumanji Patil ,02ZPENHPF7201 ,nalinipo81@gmail.com,7499928645
10,Bramhapuri,Udapur,Gopal wasudev Gawture, कंत्राटी ग्रा. प. अ,gopalgowture@gmail.com,7620462016
11,Bramhapuri,chichkeda /kalmgaon ,Hemraj mukharu mane ,02ZPEHMMM8102,manehemraj @gmail. com ,9763836323
12,Bramhapuri,Chichgaon /Kosambi khad,Bhumika bhagwan Akhade ,02ZPEBBAF8601,bhumikabakhade@gmail ,9405509797
13,Bramhapuri,Torgaov bk ,Akash Shridhar Kalamkar,02ZPEASKM8502,akash.kalamkar26@gmail.com,9921991944
14,Bramhapuri,kudesaoli /Bodadha /Ballarpur ,Chandrashekhar Narayan Patil ,02ZPECNPM7601,nayanpatil670@gmail.com,8551847343
15,Bramhapuri,Ekara ,SachinKumar Bhawarlal Raut,02ZPESBRM8601,SachinKumarraut9@gmail.com,7796839559
16,Bramhapuri,Betala / Bodhegaon ,Kishor Satyafula Tatoba Ramteke,02ZPEKTRM8001,kishorramteke80@gmail.com,9403292878
17,Bramhapuri,Wandra / Aksapur,Rushishwar Powtuji Aurase,02ZPERPAM8301,rushiaurase1@gmail.com,9404216716
18,Bramhapuri,Mudza ,Rajendra Girmaji Yerme,02ZPERGYM7801,anushkayerme@gmail.com,7721940806
19,Bramhapuri,Zilbodi ,Shiwani Ashok Waghare , कंत्राटी ग्रा. प. अ,shiwaniwaghare5@gmail ,9112696525
20,Bramhapuri,Mangli,Anandrao shreeram Thakare ,02ZPEASTM 7001 ,anandthakare12@gmail.com,9284139476
21,Bramhapuri,Chandgaon /Maldogri ,minakshi Narendra Raut ,02ZPEMNRF8801,minakshi2514@gmail.com,9423667860
22,Bramhapuri,Rui,Ranjit  Premlal Nandeshwar ,02ZPERPNM8201,nandu3474@gmail.com,8788952950
23,Bramhapuri,Waygaon,Chhabila Gajanan Giradkar ,02ZPECGGF7901,chhabilagiradkar@gmail.com,7507601915
24,Bramhapuri,Awalgaon /Pachgav ,Pradeep Laxman Talmale,02ZPEPLTM6901,pradeeptalmale5282@gmail.com,7972382206
25,Bramhapuri,Belgaon Jani /Torgaon khurd ,Mangesh Vijay Gowardhan ,02ZPEMVGM9001,mgowardhan90@gmail.com ,9604525590
26,Bramhapuri,Kolari,Ganesh Rushiji Churhe,02ZPEGRCM8901,ganesh44churhe@gmail.com,8275215053
27,Bramhapuri,Gogaon ,Hiralal Shamrao Bangare ,02ZPEHSBM7401,hiralalbangare@gmail.com,9834242821
28,Bramhapuri,Rampuri ,Sunil pundalik bangare ,02ZPESPBM7405,sunilbangare5555@gmail.com,9763437246
29,Bramhapuri,borgon ,Gopal Wasudev Gawture , कंत्राटी ग्रा.पं.अ ,gopal gawture@gmail.com,7620462016
30,Bramhapuri,Arhernavargaon ,Ratiram Bhimak Chaudhari ,02ZPEGRCM7502,chaudhariratiram08@gmail.com ,8788732105
31,Bramhapuri,Bhaleshwar ,Ratiram Bhimak Chaudhari ,02ZPEGRCM7502,chaudhariratiram08@gmail.com ,8788732105
32,Bramhapuri,khandala ,Prashant  Natthuji Masane ,02ZPEPNMM7901,prashant. masane358@gmail.com,7498620362
33,Bramhapuri,Kahali ,Prashant Natthuji Masane ,02ZPEPNMM7901,prashant.masane358@gmail.com,7083608823
34,Bramhapuri,Khedmakta,Ramkrushna Marotrao Kamdi,02ZPERMKM6803,ramkrushnakamdi17@gmail.com,9823536842
35,Bramhapuri,Mendki ,Arvind Wamanrao Lanjewar ,02ZPEAWLM7101,arvindwlanjewar@gmail.com,9158479355
36,Bramhapuri,Lakhapur ,Bhumeshwar Waman Hume ,02ZPEBWHM8101,humebhumeshwar78@gmail.com ,8275724662
37,Bramhapuri,Adyal jani/chandali,Pramod lalaji Bhoyar,02ZPEPLBM7502,plbhoyart@gmil.com,9765238199
38,Bramhapuri,Mararmendha,Pallavi Chandrakant Chaudhari,02ZPEPCCF8801,pallavi2chaudhari@gmail.com,8806260741
39,Bramhapuri,Maher,Pallavi Chandrakant Chaudhari,02ZPEPCCF8801,pallavi2chaudhari@gmail.com,8806260741
40,Bramhapuri,Mui,Sanjiv Damodhar Thakare ,02ZPESDTM7301,sanju.thakare.94@gmail.com,9404641289
41,Bramhapuri,Ranbothali,Pundalik Gajanan Thakare,02ZPEPGTM7901,pundalikthakare@gmail.com,9421856838
42,Bramhapuri,Chakbothali,Pundalik Gajanan Thakare,02ZPEPGTM7901,pundalikthakare@gmail.com,9421856838
43,Bramhapuri,Bardakinhi ,Homdeo Baburao Talande ,02ZPEHBTM7401,hbtalande@gmail.com,7972704961
44,Bramhapuri,Halda ,Homdeo Baburao Talande ,02ZPEHBTM7401,hbtalande@gmail.com,7972704961
45,Bramhapuri,Jugnala ,Ashwini Kanhaiya Kayarkar, कंत्राटी ग्रा.पं.अ ,ashwinikayarkar12@gmail.com,9156124068
46,Bramhapuri,kharkada,Hemant damodhar ramteke ,02ZPEHDRM7701,hemantramteke123@gmail.com,9527083702
47,Bramhapuri,Dighori,Josna Tekram Lanje, कंत्राटी ग्रा.पं.अ ,josnatekramlanje@gmail.com,7378491830
48,Bramhapuri,kaleta ,Shailesh Ramchandra Sahare ,02ZPESRSM7606,shailesh.sahare51@gmail.com,9405159704
49,Bramhapuri,kinhi,sadhana Pramod Diwate,02ZPESPDF8002,sadhanadiwate1980@gmail.com,7498163854
50,Bramhapuri,Gangalwadi ,Sanjiv Damodhar Thakare ,02ZPESDTM7301,sanju.thakare.94@gmail.com,9404641289
51,Bramhapuri,Talodhi (Khurd),Devendra Tulshiram Sapate,02ZPEDTSM7801,devasapate7@gmail.com,9518783731
52,Bramhapuri,Chikhalgaon,Dadhana Pramod Diwate,02ZPESPDF8002,sadhanadiwate1980@gmail.com,7498163854
53,Bramhapuri,Nanhori,Bhushan Naresh Pilare,कंत्राटी ग्रा. प. अ.,Bnpilare@gmail.com,8830030388
54,Bramhapuri,sondri/surbodi,prakash sitaram tondare,02ZEPSTM7801,prakashtonare755@gmail.com,9673038761
55,Bramhapuri,saigaon,sandip dadaji nahale ,02ZPESDNM8601,sandipnahale786@gmail.com,9049530012
56,Bramhapuri,Jawarabodi Mendha ,Kishor Rambhau Anole ,02ZPEKRAM8201,kishoralone93@gmail.com,9421734986
57,Bramhapuri,Chaugan,Vilas Daulat Chaudhari,02ZPEVDCM6801,vdchaudhari99@gmail.com,9518599710
58,Bramhapuri,Pimpalgaon ( Bho)/Ladaj,Madhukar Shrihari Ghule ,02ZPEMSGM6801,ghulemadhukar6@gmail.com,9623210313
59,Bramhapuri,Tulanmendha,Manisha Wamanrao Mahakalkar,02ZPEMWMF7701,manishamahakalkar77@gmail.com,9823427145
60,Bramhapuri,Nilaj,Lankeshkumar Bhaiyalal Marskolhe,02ZPELBMM8101,lankeshkumarmaraskolhe@gmail.com,7720881426
61,Bramhapuri,,,,,
62,Bramhapuri,,,,,
63,Bramhapuri,,,,,
64,Bramhapuri,,,,,
65,Bramhapuri,,,,,
66,Bramhapuri,,,,,
67,Bramhapuri,,,,,
68,Bramhapuri,,,,,
69,Bramhapuri,,,,,
70,Bramhapuri,,,,,
71,Bramhapuri,,,,,
72,Bramhapuri,,,,,
73,Bramhapuri,,,,,
74,Bramhapuri,,,,,
75,Bramhapuri,,,,,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Ballarpur,Amdi,Shailesh Dayal Ramteke,02ZPESDRM7502,Shilesh29@gmail.com,7218621180
2,Ballarpur,Kalamna,Shailesh Dayal Ramteke,02ZPESDRM7502,Shilesh29@gmail.com,7218621180
3,Ballarpur,Bamni (d),Ganesh Pandurang Parsutkar,02ZPEGKPM8501,pasutkar1021ganesh@gmail.com,7767081016
4,Ballarpur,Kothari,Ganesh Pandurang Parsutkar,02ZPEGKPM8501,pasutkar1021ganesh@gmail.com,7767081016
5,Ballarpur,Nandgaon (pode),Nayanpal Prabhakar Dudhe,02ZPENPDM7901,nayanpaldudhe@gmail.com,9405987115
6,Ballarpur,Hadasti,Nayanpal Prabhakar Dudhe,02ZPENPDM7901,nayanpaldudhe@gmail.com,9405987115
7,Ballarpur,Gilbili,Sushama Moreshwar Nandeshwar,02ZPESMNF8001,sushmakarwade69@gmail.com,9420011566
8,Ballarpur,Manora,Sushama Moreshwar Nandeshwar,02ZPESMNF8001,sushmakarwade69@gmail.com,9420011566
9,Ballarpur,Kawadzai,Milind Haridas Devgade,02ZPEMHDM7701,deogade.milind@gmail.com,9767594909
10,Ballarpur,Korti Makta,Milind Haridas Devgade,02ZPEMHDM7701,deogade.milind@gmail.com,9767594909
11,Ballarpur,Palasgaon,Milind Haridas Devgade,02ZPEMHDM7701,deogade.milind@gmail.com,9767594909
12,Ballarpur,Visapur,Ganesh Jairam Kokode,02ZPEGJKM7901,ganeshkokode10@gmail.com,9420446819
13,Ballarpur,Kinhi,Vikas Sudhakar Borewar,02ZPEVSBM7301,vsborewar@gmail.com,9850322437
14,Ballarpur,Itoli,Vikas Sudhakar Borewar,02ZPEVSBM7301,vsborewar@gmail.com,9850322437
15,Ballarpur,Daheli,Isha Sunil Wadaskar,,ishawadaskar9@gmail.com,7620501676
16,Ballarpur,Lawari,Isha Sunil Wadaskar,,ishawadaskar9@gmail.com,7620501676
17,Ballarpur,Katwali (bamni),Sunil Shamrao Kumare,02ZPESSKM7808,Sunilkumare1803@gmail.com,9172943095
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),Remarks
1,Rajura,AHERI,Bhaurao mondigi kubade ,02ZPEBMKM7702,kubadebhaurao77@gmail.com ,8208920406,
2,Rajura,ANTARGAON,Nikhil Babulala Dange ,02ZPENBDM8301,nikhildange83@gmail.com,9011221181,
3,Rajura,ARVI,Vithoba Dhonduji Dhurve ,02ZPEVDDM7001,vithobadhurve@gmail.com,9822924259,
4,Rajura,BAMANWADA,Prajwal Raju Turankar,Kantrati G.A.,Prajwalturankar2005@gmail.com,9822238595,Data Missing
5,Rajura,BHEDODA,Balwant Karnuji  warhate ,02ZPEBKWM7601,bwarhate@gmail.com,9075964030,
6,Rajura,BHENDALA,Santosh Ramaji Sakhare,02ZPESRSM7605,parimalsakhare@gmail.com ,8999648974,
7,Rajura,BHENDVI,Ashish Namdevrao Chatreshwar ,02ZPEANCM7901,Chatreshwarashish@gmail.com,8999503790,
8,Rajura,BHURKUNDA BK,Balwant Karnuji  warhate ,02ZPEBKWM7601,bwarhate@gmail.com,9075964030,Duplicate
9,Rajura,BHURKUNDA KH,Kalyani Madhukar Parkhi,Kantrati G.A.,kalyaniparkhi03@gmail.com,9284112615,Data Missing
10,Rajura,CHANAKHA,Nisha Shivlal Kaliwale,02ZPENSKF9202,nishakaliwale1@gmail.com,9511604886,
11,Rajura,CHANDANWAHI,Anil Fulsing Jadhav,02ZPEAFJM7601,aniljadhao8136@gmail.com,9823499845,Already Present
12,Rajura,CHARLI,Vivek Rajabhau Walke,02ZPEVRWM8601,vevswalke@gmail.com,8830616356,Already Present
13,Rajura,CHINCHOLI BK.,Santosh Ramaji Sakhare,02ZPESRSM7601,parilamsakhare@gmail.com ,8999648974,Already Present
14,Rajura,CHINCHOLI KHU.,Shubhangi Krishnarao Kalwalkar,02ZPESKKF7903,shubhangikawalkar79@gmail.com,9511627971,Already Present
15,Rajura,CHUNALA,Sachin Tulsiram Virutkar,02ZPESTVM7401,virutkarsachin21@gmil.com,9765246810,
16,Rajura,DEWADA,Ashish Namdevrao Chatreshwar ,02ZPEANCM7901,Chatreshwarashish@gmail.com,8999503790,
17,Rajura,DHANORA,Manish Madhukarrao Aswale,02ZPEMMAM7801,manishaswale1@gmail.com,7447535639,
18,Rajura,DHIDASI,Prajakta Ashokrao Adgokar  ,02ZPEPAAF8401,pndaware@gmail.com,9403307778,Already Present
19,Rajura,DHOPATALA,Harshawardhan Nilkanth Khobragade ,02ZPEHNKM7903,khobragade.harsh@yahoo.in,9823438616,
20,Rajura,DONGARGAON SU,Bhujang Bhanudas Akrape,Kantrati G.A.,bhujangakrape@gmail.com,8817997321,Data Missing
21,Rajura,GOWRI,Pravin Murlidhar Ghume,02ZPEPMGM7301,ghumepravin9873@gmail.com,9421970131,
22,Rajura,GOYEGAON,Vijay Haribhau Satpute,02ZPEVHSM8002,vhs1851@gmail.com,9405136140,Already Present
23,Rajura,HARDONA KH.,Mahesh Shankar Marape ,02ZPEMSMM9402,maheshmarape89@gmail.com,9673099353,Already Present
24,Rajura,ISAPUR,Rohan Diwakar Gedam,Kantrati G.A.,gedamrohan217@gmail.com ,7507916370,Data Missing
25,Rajura,JAMNI,Nagesh Sanjay Madavi ,Kantrati G.A.,nageshmadavi01@gmail.com,9673768042,Data Missing
26,Rajura,KADHOLI BK,Premdas Gabbuji Rathod,02ZPEPGRM8502,premdasrathod87@gmail.com,8830616356,Already Present
27,Rajura,KALMNA,Ekanath Arjun Meshram ,02ZPEEAMM7901,eknathmeshram61548@gmail.com,9823940525,
28,Rajura,KAVITHPETH,Manish Madhukarrao Aswale,02ZPEMMAM7801,manishaswale1@gmail.com,7447535639,Duplicate
29,Rajura,KAWADGONDI,Madhuri vinod meshram ,Kantrati G.A.,madhurimeshram112233@gmail.com,7378489006,Data Missing
30,Rajura,KHAMONA,Vinod  Namdevrao Kewe,02ZPEVNKM7701,vinodkewe77@gmail.com,7776863099,Already Present
31,Rajura,KOHPARA,Rajesh Vilasrao Maske,02ZPERVMM8801,Mraj0871@gmail.com,9130401175,
32,Rajura,KOLGAON,Asha Bhairao Ramteke,02ZPEABRF8401,asharamteke7@gmail.com,9545255152,Already Present
33,Rajura,KOSHTALA,Renuka Manoharrao Deo,Kantrati G.A.,renukatopre4@gmail.com,8975738559,Data Missing
34,Rajura,LAKKADKOT,Purushottam Ramprasad Mishra,02ZPEPRMM7202,mishrapurushottam92@gmail.com ,8637763315,Already Present
35,Rajura,MANGI BK,Nandini.Shankar.Korwate,Kantrati G.A.,korwatenandini@gmail.com,7796845106,Data Missing
36,Rajura,MANOLI BK,Ekanath Arjun Meshram ,02ZPEEAMM7901,eknathmeshram61548@gmail.con,9823940525,Already Present
37,Rajura,MANOLI KH,Pavan Vasant Wasekar ,02ZPEPVWM8301,pavanwasekar11111@gmail.com,8308664993,Already Present
38,Rajura,MARDA,Nilesh Haridas Daware,02ZPENHDM8101,ndaware2@gmail.com,9923930623,Already Present
39,Rajura,MURTI,Hitendra sudam girsawle ,02ZPEHSGM8201,hitendragirsawale45@gmail.com,9423410040,
40,Rajura,MUTHARA,Anil Fulsing Jadhav,02ZPEAFJM7601,aniljadhao8136@gmail.com,9823499845,Already Present
41,Rajura,NALFADI,Minakshi Wasudeo Bodekar ,02ZPEMWBF8201,meenakshibodekar@gmail.com,9923111072,Already Present
42,Rajura,NOKARI KH,Pavan Vasant Wasekar ,02ZPEPVWM8301,pavanwasekar11111@gmail.com,8308664993,Already Present
43,Rajura,PACHGAON,Vijay Haribhau Satpute,02ZPEVHSM8002,vhs1851@gmail.com,9405136140,Already Present
44,Rajura,PANCHALA,Rajesh Vilasrao Maske,02ZPERVMM8801,sangrampanchala21@gmail.com,9130401175,Already Present
45,Rajura,PANDHARPOUNI,Bhaurao mondigi kubade ,02ZPEBMKM7702,kubadebhaurao77@gmail.com ,9011583378,Already Present
46,Rajura,PELLORA,Nilesh Haridas Daware,02ZPENHDM8101,ndaware2@gmail.com,9923930623,Already Present
47,Rajura,POUNI,Pravin Murlidhar Ghume,02ZPEPMGM7301,ghumepravin9873@gmail.com,9421970131,Already Present
48,Rajura,RAMPUR,Sachin Tulsiram Virutkar,02ZPESTVM7401,virutkarsachin21@gmil.com,9765246810,Already Present
49,Rajura,SAKHARI,Vandana Uddhao Mathankar,02ZPEVUMF7301,vandanamathankar73@gmail.com,9922775656,Duplicate
50,Rajura,SAKHARWAHI,Tarachand Devrao Nandanwar ,02ZPETDNM7901,nandanwartarachand@gmail.com,8554889356,Already Present
51,Rajura,SASTI,Sanjay Laxman  Atram,02ZPESLAM7101,sanjuat71@gmail. com,7776988251,Already Present
52,Rajura,SATRI,Prajwal Raju Turankar,Kantrati G.A.,Prajwalturankar2005@gmail.com,9822238595,
53,Rajura,SINDHI,Minakshi Wasudeo Bodekar ,02ZPEMWBF8201,meenakshibodekar@gmail.com,9923111072,Already Present
54,Rajura,SIRSI,kalyani sudhakar bangare,Kantrati G.A.,kalyanibangare44@gmail.com,9284395231,
55,Rajura,SONAPUR,Rohan Diwakar Gedam,Kantrati G.A.,gedamrohan217@gmail.com ,7507916370,
56,Rajura,SONDO,Nisha Shivlal Kaliwale,02ZPENSKF9202,nishakaliwale1@gmail.com,9511604886,
57,Rajura,SONURLI,Amol Banduji Badkhal ,02ZPEABBM8901,amolbadkhal59@gmil.com,7972996439,
58,Rajura,SUBAI,Nikhil Babulala Dange ,02ZPENBDM8301,nikhildange83@gmail.com,9011221181,Already Present
59,Rajura,SUMTHANA,Vithoba Dhonduji Dhurve,02ZPEVDDM7001,vithobadhurve@gmail.com,9822924259,Already Present
60,Rajura,TEMBHURWAHI,Amol Bandu  Badkhal,02ZPEABBM8901,amolbadkhal59@gmil.com,7972996439,
61,Rajura,VIHIRGAON,Hitendra sudam girsawle ,02ZPEHSGM8201,hitendragirsawale45gmail.com,9423410040,Already Present
62,Rajura,VIRUR STATION,Tarachand Devrao Nandanwar ,02ZPETDNM7901,nandanwartarachand@gmail.com,8554889356,
63,Rajura,WARODA,Vandana Uddhao Mathankar,02ZPEVUMF7301,vandanamathankar73@gmail.com,9922775656,
64,Rajura,WARUR ROAD,Vinod  Namdevrao Kewe,02ZPEVNKM7701,vinodkewe77@gmail.com,7776863099,Already Present
65,Rajura,YERGAVHAN,Madhuri Vinod meshram ,Kantrati G.A.,madhurimeshram112233@gmail.com,7378489006,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),
1,GondPipari,"Sakmur, Watrana",r,02ZPERRNM8601,www.radhakrushna1986@gmail.com,9527480056,
2,GondPipari,"Hiwra,Panora,Chekpargaon,Sonapur Desh",Prabhudas Devidas Raut,02ZPEPDRM8401,www.rautprabhudas1923@gmail.com,9922353836,
3,GondPipari,Ganeshpipari,Magesh Namdeo Durge,02ZPEMNDM8301,mangeshdurge5@gmail.com,8329193227,
4,GondPipari,"Aksapur,Karanji",Sunita Kedar Kancharlawar,02ZPESKKF7604,sunitakancharlawar@gmail.com,9359088598,
5,GondPipari,"Dhamangaon,Supgaon",Mangala Atmaram Aknurwar,02ZPEMAAF7801,dingalwarmangla@gmail.com,9552468267,
6,GondPipari,Dhaba,Gajanan Bhausaheb Ghuge,02ZPEGBGM8901,www.gajananghuge77@gmail.com,8999423461,
7,GondPipari,"Salezari,Darur",Prabhakar Sambanaji Perkiwar,02ZPEPSPM7505,perkiwarprabhakar@gmail.com,7767843649,
8,GondPipari,"Ghadoli,Chekghadoli",Alka Meghshyam Salve,02ZPEAMSF8601,alkakankate39@gmail.com,7875475342,
9,GondPipari,"Vihirgaon,Gojoli,Chek Pipari",Sadhna Hanmantu Pendharkar,02ZPESHPF8101,sadhanapedharkar540@gmail.com,8007149216,
10,GondPipari,Somanpalli,Mamta Vilas Bakshi,02ZPEMVBM8501,mamtabakshi358@gmail.com,9403875093,
11,GondPipari,"Tarda,Furdiheti,Chek Borgaon",Devanad Murlidhar Gedam,02ZPEDMGM7201,www.dewagedam72@gmail.com,9049624313,
12,GondPipari,"Chekdarur,Kirmiri",Waman Ganbaji Choudhari,02ZPEWGCM7301,wamnachoudhari11@gmail.com,9146108820,
13,GondPipari,Lathi,Manjusha Marotrao Parkhi,02ZPEMMPF8304,www.manjushparkhi1983@gmail.com,7030205964,
14,GondPipari,Tohogaon,Sanjay Sheshrao Golarwar,02ZPESSGM7304,sanjaygollarwar339@gmail.com,9604367494,
15,GondPipari,"Adegaon,Cheknandgaon,Nandwardhan",Santosh Sudhakar Ghate,02ZPESSGM7605,santoshghate18@gmail.com,9067493554,
16,GondPipari,Bhangaram Talodhi,Raju Madhukar Kapkar,02ZPERMKM7302,rajukapkar576@gmail.com,9421718244,
17,GondPipari,Wejgaon,Usha Govinda Tembhurne,02ZPEUGTF7901,deogade.ushamilind@gmail.com,9075986900,
18,GondPipari,"Tarsa Buj, Vitthalwada",Lina Sarangdhar Meshram,02ZPELSMF8601,meshramleena195@gmail.com,7498767832,
19,GondPipari,Kanhalgaon,Manohar Vitthal Choudhari,02ZPEMVCM7401,choudharimanohar0@gmail.com,7350245700,
20,GondPipari,"Kudesavli,Parsodi",Jitendra Fulchand Khobragade,02ZPEJFKM7601,jeetanjali19@gmail.com,9765559768,
21,GondPipari,Chek Dubarpeth,Narendra Balaji Barsagade,02ZPENBBM8101,narendrabarsagade2@gmail.com,9923690884,
22,GondPipari,"Wadholi,Kharalpeth",Anil Namdeo Haramwar,02ZPEANHM7301,anilharamwar@gmail.com,9309704880,
23,GondPipari,Chek Berdi,Bhujang Ramrao Suryavanshi,02ZPEBRSM7201,bhujangsuryawanshi@gmail.com,8087258240,
24,GondPipari,Dhanapur,Ravi Kavduji Bodhe,02ZPERKBM8501,ravibodhe1234@gmail.com,9975967125,
25,GondPipari,chek likhitwada,Sanjay Patruji Ade,,adesnjay93@gmail.com,9359235556,कंत्राटी ग्रामपंचायत अधिकारी
26,GondPipari,"Nandgaon,",Dinesh Diwakar Dehankar,02ZPEDDDM8301,dehankardinesh23@gmail.com,8080646878,
27,GondPipari,,Radha Gundopant Hinje,02ZPERGHF9001,radha.hinje@gail.com,9405467725,
28,GondPipari,,Krupanand Gajanan Bagale,02ZPEKGBM7501,bkgb1975@gmail.com,9284327769,
29,GondPipari,,Ujwala Rushiji Urade,02ZPEURUF8301,ujwalaurade352@gmail.com,9209680354,
30,GondPipari,,Vilas Balaji Bhoyar,02ZPEVBBM6801,vilas.bhoyar@gmail.com,9309396585,On Medical Leave
31,GondPipari,,Vitthal Shamrao Tiwade,02ZPEVSTM6702,vitthal.tiwade@gmail.com,7588911319,Retirenment on 31.12.2025
32,GondPipari,Dongargaon,Magesh Namdeo Durge,02ZPEMNDM8301,mangeshdurge5@gmail.com,8329193227,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Pombhurna,ghatkul ,Ashish Shankar Ankanurwar ,02ZPEASAM8302,Gp.thergaon1961@gmail.com,9921657776
2,Pombhurna,Ghosari,Swaraj Ganesh Pidurkar ,kantranti karmachari,pidurkarswaraj@gmail.com,8857928873
3,Pombhurna,Pipari Deshpande ,Sachin Shankar Ade,02ZPESSAM8901,sachinade34@gmail.com,9420367667
4,Pombhurna,Chakthana ,Sachin Shankar Ade ,02ZPESSAM8901,sachinade34@gmail.com,9420367667
5,Pombhurna,Chak Thanewasana ,Ketan Dhaneshwar Ramteke,kantranti karmachari,kgspombhurna@gmail.com,7888148373
6,Pombhurna,Ashta ,Manoj Vasantrao Mudawar ,02ZPEMVMM7803,mmudawar3255@gmail.com,7588806394
7,Pombhurna,Chek. Ashta ,Manoj Vasantrao Mudawar ,02ZPEMVMM7803,mmudawar3255@gmail.com,7588806394
8,Pombhurna,Chek Ambedhanora ,Rajesh Vishwanath Ture ,02ZPERVTM7601,rajeshvishwanathture@gmail.com,9763076399
9,Pombhurna,Chek Hattibodi ,Surekha Laxman Madavi ,02ZPESLMF7202,surekhamadavi44@gmail.com,8411089741
10,Pombhurna,Bhimni ,Haridas vithal Bhasarkar ,02ZPEHVBM7301,Piyusharidas12@gmeal.c ,9673897167
11,Pombhurna,mohala ryt,vidhya santosh pawar ,kantranti karmachari,vidhyaspawar1212@gmail.com,8459468454
12,Pombhurna,Kasargatta ,Pravin Divakar Kadukar ,02ZPEPDKM7902,pravinkadukar1979@gmail.com,9923111120
13,Pombhurna,Borda Zullurwar ,Pravin Divakar Kadukar ,02ZPEPDKM7902,pravinkadukar1979@gmail.com,9923111120
14,Pombhurna,chintaldhaba ,Anand Prakash Katkamwar ,02ZPEAPKM8801,anandkatkamwar@gmail.com,9527864089
15,Pombhurna,Jamtukum,Tarachand Nilkanth Shende,02ZPETNSM7402,tnshende01@gmail.com,9763728068
16,Pombhurna,FUTANA MOKASA ,PRAMOD MURARI SARKAR,02ZPEPMSM9002,sarkarpramod96@gmail.com,9420229996
17,Pombhurna,CHAK FUTANA ,PRAMOD MURARI SARKAR,02ZPEPMSM9002,sarkarpramod96@gmail.com,9420229996
18,Pombhurna,DEWADA BK,PRAMOD MURARI SARKAR,02ZPEPMSM9002,sarkarpramod96@gmail.com,9420229996
19,Pombhurna ,Dighori ,Arun Waduji Mashakhetri ,02ZPEAWMM7101,arunmashakhet ri1971@gmail,8788055043
20,Pombhurna ,Ghanoti tukum,Santosh Latari Parsutkar,02ZPESLPM7801,gpghanotitukum@gmail.com,9834891853
21,Pombhurna ,Borda Borkar,Santosh Latari Parsutkar,02ZPESLPM7801,gpghanotitukum@gmail.com,9834891853
22,Pombhurna,Thergaon ,Ashish Shankar Ankanurwar ,02ZPEASAM8302,Gp.thergaon1961@gmail.com,9921657776
23,Pombhurna ,Navegaon More,Jidnyasa Diwakar Pendor,kantranti karmachari,pendorjidnyasa50@gmail.com,9309206457
24,pombhurna ,devada khurd ,Dilip Maroti Shinde ,02ZPEDSM6903,dilip shinde2369@gail.com,9420300227
25,POMBHURNA,JAM KHURD,SHUBHASH RAMAJI TELMASARE,02ZPESRTM7402,subhastelmasare74@gmail.com,9637565153
26,POMBHURNA,JUNGOAN,SHUBHASH RAMAJI TELMASARE,02ZPESRTM7402,subhastelmasare74@gmail.com,9637565153
27,POMBHURNA,KEMARA,DEVENDRA BALKRUSHNA BAMBOLE,02ZPEDBBM7102,devendrabambole111@gmail.com,9765048951
28,POMBHURNA,SATARA BHOSALE,VINOD GOPICHAND CHIMURKAR,02ZPEVGCM7401,vinodchimurkar015@gmail.com,9763980596
29,POMBHURNA,WELWA,VINOD GOPICHAND CHIMURKAR,02ZPEVGCM7401,vinodchimurkar015@gmail.com,9763980596
30,POMBHURNA,UMARI POTDAR,PRAMOD RAJESHWAR TIMANDE,02ZPEPRTM7801,pramodtimande31@gmail.com,7588658320
31,POMBHURNA,CHEK BALLARPUR,PRAMOD RAJESHWAR TIMANDE,02ZPEPRTM7801,pramodtimande31@gmail.com,7588658320
,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory),,,,,
1,Korpana,khayrgav ,Arun Janga Meshram,"02ZPEAJMM8702	
",arunmeshram87@gimel.com ,9511747828,,,,,
2,Korpana,matha ,Dilip Chaturdas Taksande,02ZPEDCTM6901,diliptaksande75@gmail.com,8805147881,,,,,
3,Korpana,Wadgaon,Dhirajkumar Nanaji Borkar ,02ZPEDNBM8001,dhirajkumarborkar@gmail.com,9552215252,,,,,
4,Korpana,nimni ,Subhash Purushottam Saraye,02ZPESPSM8501,subhashsaraye@gmail.com,9673036037,,,,,
5,Korpana,jevra ,sangesh uttam shinde ,02ZPESUSM8503,sangeshshinde1@gmail.com,8275246004,,,,,
6,Korpana,Naranda ,Laxman Ram misal ,02ZPELRMM8401,Laxmanmisal84@gmail.com,8928618777,,,,,
7,Korpana,chanai bk ,sanjay vasaram ade ,02ZPESVAM8401,sanjayade1985@gmail.com,8975794195,,,,,
8,Korpana,nanda,naresh Gajanan Dhawne ,02ZPENGDM6904,nareshdhwane751@gmail.com,8605060133,,,,,
9,Korpana,Antargav bu ,Pankaj Sureshrao Upase ,02ZPEPSUM8501,pupase414@gmail.com,8999336978,,,,,
10,Korpana,khadholi khu,Varsha nilkhanthrao bhuyar ,002ZPEVNBF8301,varshachaudhari578@gmail.com,9545971782,,,,,
11,Korpana,kothoda bk,satish fakru madavi,02ZPESFMM8602,sat5madavi@gmail.com,8459466150,,,,,#ERROR!
12,Korpana,katlaboli ,devannd wasudev uike,02ZPEDWUM8101,devauike@gmail.com,9822063987,,,,,
13,Korpana,uparvahi ,mahesh hiraman milmile ,02ZPEMHMM7602,maheshmilmile411@gmail.com ,9011119342,,,,,
14,Korpana,bibi ,Dhanaraj Suryabhanji Dukare ,02ZPEDSDM7401,dhanrajdukare67 @ gmail ,9518576120,,,,,
15,Korpana,virur( ga ),gunja tulshiram uike ,02ZPESTUF7901,gunjauike1980@gmail. com,9405984333,,,,,
16,Korpana,kawathala ,Gopal Annaji Naitam,02ZPEGANM7901,"gopalnaitam6947@gmail, com",7378359919,,,,,
17,Korpana,bharosa ,prakash Tukaramji Shende,02ZPEPTSM6801,prakashshende315@gmail.com,7507370066,,,,,
18,Korpana,wanoja ,sandip wasudeo bodhe ,02ZPESWBM8901,bodhesandip3@gmail.com,9764270406,,,,,
19,Korpana,loni ,vijay bapurav dange ,02ZPEVBDM7102,dangevijay963@gmail. com,8975393703,,,,,
20,Korpana,lakhamapure ,amol rameshrav shinde ,02ZPARSM7901,amolshindefeb79@gmail.com,9657852906,,,,,
21,Korpana,pardi ,pyarelal parshuram dahiwale ,02ZPEPPDM8102,pyarelaldahiwale7@gmail.com,9881224818,,,,,
22,Korpana,khirdi,rajaram laxman pole,02ZPERLPM8601,rajarampole@gmail.com,9011583277,,,,,
23,Korpana, mandwa,mushtaq nawab sheikh,02ZPEMNSM6803,mushtaqueahmadsheikh@gmail,7620654576,,,,,
24,Korpana,Bakhardi,Pawan Amrut Katkar,02ZPEPAKM8601,pawan277kaatkar@gmail.com,9011227282,,,,,
25,Korpana,Sangoda,Jogeshwar Shamrao Wakade,02ZPEJSWM8201,jogeshwarwakade2015@gmail.com,9405775141,,,,,
26,Korpana,piparda,Dilip Sakharam Bawane,02ZPEPTSM6801,dilipbawane123@gmail.com,7774980820,,,,,
27,Korpana,Nandgaon,Ramdas Uttmrao Rathod,0ZPERURM8301,Ramdas  Rathod465@gmail.com,8668875853,,,,,
28,Korpana,talodi ,sanjay sonbaji turare,02ZPESSTM7502,sanjayturare1975@gmail.com,9423423694,,,,,
29,Korpana,p.s.korpana,sangharsha vishanu gaikwad,,sangharshagaikwad@gmail.com,8275304519,,,,,
30,Korpana,Mangal Hira,Pradip Vikas Bhavar,-,bhavarpradip0@gmail.com,9834877281,,,,,
31,Korpana,Vadgaon ,Sweeti Janrdan Nagrale ,-,nagralesweeti@gmail.com,9834562397,,,,,
32,Korpana,sawarhira ,Krishna Datta Uike,-,krishnauike687@gmail.com,8378935300,,,,,
33,Korpana,rupapeth,Ashvina Bhaurao Kulmethe,-,ashvinikulmethe48@gmail.com,8799843468,,,,,
34,Korpana,Kukudsath ,dinesh jangu kotnake,-,kotnakedinesh3@gmail.com,7498975434,,,,,
35,Korpana,durgali ,tejrao ramdas satpute,-,tejraosatpute4@gmail.com,9373571415,,,,,
36,Korpana,belgaon,Achal Murlidhar Sidam ,-,sidamachal82@gmail.com,7499311991,,,,,
37,Korpana,dhanoli ,prajvl dilip jamdale,-,jamdaleprajwa120@gmail. com,7768822189,,,,,
38,Korpana,yergavhan ,sachin maroti gedam ,-,sachingedam97@gmail.com ,9011424758,,,,,
39,Korpana,kanhalgaon ,roshan gangadhar nimje ,-,roshannimje464@gmail.com,7384809636,,,,,
40,Korpana,Parsoda ,Anil Ramdas Kotnake ,-,anilkotnake968@gmail.com,8552998096,,,,,
41,Korpana,Awalpur,Dhirajkumar Nanaji Borkar ,,dhirajkumarborkar@gmail.com,9552215252,,,,,
42,korpana ,durgadi ,Tejrao Ramdas Satpute ,-,tejraosatpute4@gmail.com,9373571415,,,,,
,korpana ,KODSHI BK ,sangesh uttam shinde ,,sangeshshinde1@gmail.com,8275246004,,,,,
,korpana ,sheraj kh,Rajaram Laxman pole,02ZPERLPM8601,rajarampole@gmail.com,9011583277,,,,,
,korpana ,Sheraj Bk,Rajaram Laxman Pole ,02ZPERLPM8601,rajarampole@gmail.com,9011583277,,,,,
,korpana ,thutra ,mahesh hiraman milmile ,,maheshmilmile411@gmail. com,9011119342,,,,,
Sr. No.,Block Name,Gram Panchayat Name,Gram Sewak's Full Name,Sewarth ID (Compulsory),Email ID (Compulsory),Mobile No. (Compulsory)
1,Jiwati,Lambori ,Sanket Suryabhan Chahakate ,,sanketchahakate@gmail.com,9284426644
2,Jiwati,dhankdevi ,Raghu Dharma Madavi ,,raghumadavi5@gmail.com,8390976125
3,Jiwati,Nokewada ,Hansraj Waman Marape ,,hansrajmarape86@gmail.com,9049390617
4,Jiwati,bhoksapur ,kishor lahuji dhapkas ,02ZPEKLDM8401,dhapkaskishor@gmail.com,9158478264
5,Jiwati,rahapalli khurd ,kishor lahuji dhapkas ,02ZPEKLDM8401,dhapkaskishor@gmail.com,9158478264
6,Jiwati,pittiguda no1 ,Ganesh Namdew Ghodmare ,02ZPEGNGM7301,ganeshghodmar@ gmail.com ,9158390198
7,Jiwati,Kekezari,Shrikrushna Paroji Kurude ,02ZPESPKM7405,kurudeshrikrushna@gmail.com,8767886865
8,Jiwati,Dampur mohada,Shrikrushna Paroji Kurude ,02ZPESPKM7405,kurudeshrikrushna@gmail.com,8767886865
9,Jiwati,Asapur,Gajanan Bamnaji Vanjare,02ZPEGBVM8503,gvanjare54@gmail.com,8208435038
10,Jiwati,Dewlaguda ,Gajanan Bamnaji Vanjare,02ZPEGBVM8503,gvanjare54@gmail.com,8208435038
11,Jiwati,Maraipatan ,Vikas Jeevan Suryawanshi,,vik99.vs@gmail.com,9579398848
12,Jiwati,pathan ,Shrihari kerba Kendre ,02ZPESKKM8003,shriharikendre0@gmail.com,9011359572
13,Jiwati,yermi yesapur ,sunil walmik nagrale,,nagralesunil451@gmail.com,8007884866
14,Jiwati,Markalmetta ,Umesh Prakash Suradkar ,,umeshsuradkar3@gmail.com,8975054706
15,Jiwati,Shengaon ,mohan R jogi ,02ZPEMRJM7302,mohan. jogi1973@gmail.com ,9822567332
16,Jiwati,Gudshela/pudiyal mohada ,Prashant N Lamge,02ZPEPNLM8101,prashantlamge31@gmail.com,7620928278
17,Jiwati,Kodepur,Kiran Tukaram Gaikwad,02ZPEKTGM8701,Kiran.gaikwad501@gmail.com,7498882885
18,jiwati ,Shedwahi(La),Kiran Tukaram Gaikwad ,02ZPEKTGM8701,kiran.gaikwad501@gmail.com,7498882885
19,Jiwati,Yelapur,Kiran Tukaram Gaikwad ,02ZPEKTGM8701,kiran.gaikwad501@gmail.com,7498882885
20,jiwati ,chikhali bk ,prakash kawadu borkar ,02ZPEPKBM7901,prakashborkar250@gmail.com,9158584179
21,jiwati,pittiguda 02,Vijay Ramchandra Madavi,,vjmadavi1985@gmail.com,8766951291
23,Jiwati,shedwahi (bhari),Ravi Prabhakar Borkar ,02ZPERPBM8902,borkaravi838@gmail.com,8329179741
24,Jiwati,sorekasa ,Ravi Prabhakar Borkar ,02ZPERPBM8902,borkarravi838@gmail.com,8329179741
25,Jiwati,Dhondaarjuni ,Raju Shamrao Nagulwar ,02ZPERSNM7801,rajunagulwar1978@gmail.com,8830945392
26,Jiwati ,Tekamandva ,Raju Shamrao Nagulwar ,02ZPERSNM7801,rajunagulwar1978@gmail.com,8830945392
27,Jiwati ,Ambezari,ARCHANA RAMDAS BHOYAR,02ZPEARBF8501,,
28,Jiwati,Paramdoli,DINKAR UGRAVANYA PAWARA,02ZPEDUPM8501,,
29,Jiwati,Nandappa,MUNNA KESHAO SIDAM,02ZPEMKSM8901,,
30,Jiwati ,Markagondi,YOGITA PARSHURAM CHITADE,02ZPEYPCF8901,,
31,,Kumbhezari,Vinod Sherakhi,,,
32,,Khadaki Raipur,Vinod Sherakhi,,,
33,,Khadaki Hirapur,Pradip Madavi,,,
34,jiwati,Bhari,Shrihari kerba Kendre ,02ZPESKKM8003,shriharikendre0@gmail.com,9011359572
35,,,,,,
"""

with open("raw_contacts.txt", "w", encoding="utf-8") as f:
    f.write(raw_data)
print("Saved raw_contacts.txt")
