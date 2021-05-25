-- counting: 1 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='852 North Dean Road',
			    @param_add2=null,
			    @param_city='Auburn',
			    @param_state='AL',
			    @param_zip='36830',
			    @param_country='USA',
			    @param_lat='32.6253',
			    @param_lon='-85.4617',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='SSRG001',
			    @param_email='info@chickensaladchick.com',
			    @param_phone='334-275-4578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='1.0',
			    @param_POSID=@posid;
		 




-- counting: 2 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='320 Geary St.',
			    @param_add2=null,
			    @param_city='san francisco',
			    @param_state='CA',
			    @param_zip='94102',
			    @param_country='USA',
			    @param_lat='37.7874',
			    @param_lon='-122.40899999999999',
			    @param_timezoneid='America/Los_Angeles',
			    @param_storeName='example 6',
			    @param_email='info@simplysouthernrg.com',
			    @param_phone='847-732-1841',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='7.0',
			    @param_POSID=@posid;
		 




-- counting: 3 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3070 Zelda Road',
			    @param_add2=null,
			    @param_city='Montgomery',
			    @param_state='AL',
			    @param_zip='36106',
			    @param_country='USA',
			    @param_lat='32.3542',
			    @param_lon='-86.2647',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Montgomery - Zelda',
			    @param_email='CSC-2_Zelda@chickensaladchick.com',
			    @param_phone='334-517-1378',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='2.0',
			    @param_POSID=@posid;
		 




-- counting: 4 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='36150 Emerald Coast Pkwy, Unit 111',
			    @param_add2=null,
			    @param_city='Destin',
			    @param_state='FL',
			    @param_zip='32541',
			    @param_country='USA',
			    @param_lat='30.3866',
			    @param_lon='-86.4074',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Destin',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='850-460-2888',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='7.0',
			    @param_POSID=@posid;
		 




-- counting: 5 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='5135 Sunset Boulevard, Ste A',
			    @param_add2=null,
			    @param_city='Lexington',
			    @param_state='SC',
			    @param_zip='29072',
			    @param_country='USA',
			    @param_lat='34.0066',
			    @param_lon='-81.1958',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Lexington',
			    @param_email='csc-10_lexington@chickensaladchick.com',
			    @param_phone='803-356-0146',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='10.0',
			    @param_POSID=@posid;
		 




-- counting: 6 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2370 South Hillcrest Road, Unit R',
			    @param_add2=null,
			    @param_city='Mobile',
			    @param_state='AL',
			    @param_zip='36695',
			    @param_country='USA',
			    @param_lat='30.6418',
			    @param_lon='-88.1924',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Mobile',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='251-660-0501',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='11.0',
			    @param_POSID=@posid;
		 




-- counting: 7 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='80 McFarland Blvd Unit 12',
			    @param_add2=null,
			    @param_city='Northport',
			    @param_state='AL',
			    @param_zip='35476',
			    @param_country='USA',
			    @param_lat='33.2375',
			    @param_lon='-87.5541',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Northport',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='205-409-8635',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='4.0',
			    @param_POSID=@posid;
		 




-- counting: 8 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='629 Market Street, Ste 101',
			    @param_add2=null,
			    @param_city='Chattanooga',
			    @param_state='TN',
			    @param_zip='37402',
			    @param_country='USA',
			    @param_lat='35.0487',
			    @param_lon='-85.3098',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Chattanooga - Downtown',
			    @param_email='0016@volunteerrc.com',
			    @param_phone='423-668-0098',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='16.0',
			    @param_POSID=@posid;
		 




-- counting: 9 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6517 Kitten Lake Dr. #W6',
			    @param_add2=null,
			    @param_city='Midland',
			    @param_state='GA',
			    @param_zip='31820',
			    @param_country='USA',
			    @param_lat='32.5394',
			    @param_lon='-84.8688',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Midland',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='706-221-2086',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='12.0',
			    @param_POSID=@posid;
		 




-- counting: 10 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='100 Bluefish Drive',
			    @param_add2=null,
			    @param_city='Panama City Beach',
			    @param_state='FL',
			    @param_zip='32459',
			    @param_country='USA',
			    @param_lat='30.356379999999998',
			    @param_lon='-86.15482',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Panama City Beach',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='850-233-3134',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='14.0',
			    @param_POSID=@posid;
		 




-- counting: 11 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4101 Roswell Road Ste 811',
			    @param_add2=null,
			    @param_city='Marietta',
			    @param_state='GA',
			    @param_zip='30062',
			    @param_country='USA',
			    @param_lat='33.9806',
			    @param_lon='-84.4334',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Marietta',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='770-565-3985',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='15.0',
			    @param_POSID=@posid;
		 




-- counting: 12 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='252-Z Harbison Blvd',
			    @param_add2=null,
			    @param_city='Columbia',
			    @param_state='SC',
			    @param_zip='29212',
			    @param_country='USA',
			    @param_lat='34.0722',
			    @param_lon='-81.1569',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Columbia',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='803-550-9050',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='18.0',
			    @param_POSID=@posid;
		 




-- counting: 13 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7617-C Pineville-Matthews Rd',
			    @param_add2=null,
			    @param_city='Charlotte',
			    @param_state='NC',
			    @param_zip='28226',
			    @param_country='USA',
			    @param_lat='35.0868',
			    @param_lon='-80.8481',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Charlotte - Carmel Commons',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='980-938-8482',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='20.0',
			    @param_POSID=@posid;
		 




-- counting: 14 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7924 Vaughn Road',
			    @param_add2=null,
			    @param_city='Montgomery',
			    @param_state='AL',
			    @param_zip='36116',
			    @param_country='USA',
			    @param_lat='32.3387',
			    @param_lon='-86.1786',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Montgomery - Sturbridge',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-649-4828',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='17.0',
			    @param_POSID=@posid;
		 




-- counting: 15 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7400 Abercorn Street, Suite 512',
			    @param_add2=null,
			    @param_city='Savannah',
			    @param_state='GA',
			    @param_zip='31406',
			    @param_country='USA',
			    @param_lat='32.0086',
			    @param_lon='-81.1121',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Savannah',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(912) 200-5286',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='22.0',
			    @param_POSID=@posid;
		 




-- counting: 16 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1820 Gunbarrel Rd, Ste 200',
			    @param_add2=null,
			    @param_city='Chattanooga',
			    @param_state='TN',
			    @param_zip='37421',
			    @param_country='USA',
			    @param_lat='35.0259',
			    @param_lon='-85.1562',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Chattanooga - Gunbarrel',
			    @param_email='0019@volunteerrc.com',
			    @param_phone='423-468-3729',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='19.0',
			    @param_POSID=@posid;
		 




-- counting: 17 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='970 North point Drive, Ste B190',
			    @param_add2=null,
			    @param_city='Alpharetta',
			    @param_state='GA',
			    @param_zip='30022',
			    @param_country='USA',
			    @param_lat='34.05',
			    @param_lon='-84.2842',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Alpharetta',
			    @param_email='CSC-21_Alpharetta@chickensaladchick.com',
			    @param_phone='770-667-5459',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='21.0',
			    @param_POSID=@posid;
		 




-- counting: 18 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='975 Airport Rd SW Ste J1',
			    @param_add2=null,
			    @param_city='Huntsville',
			    @param_state='AL',
			    @param_zip='35802',
			    @param_country='USA',
			    @param_lat='34.69',
			    @param_lon='-86.5763',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Huntsville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='256-213-1067',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='23.0',
			    @param_POSID=@posid;
		 




-- counting: 19 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='210 Doug Baker Boulevard, Suite 200',
			    @param_add2=null,
			    @param_city='Birmingham',
			    @param_state='AL',
			    @param_zip='35242',
			    @param_country='USA',
			    @param_lat='33.4093',
			    @param_lon='-86.6659',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Birmingham - Lee Branch',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(205) 995-2525',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='24.0',
			    @param_POSID=@posid;
		 




-- counting: 20 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='425 Ernest Barrett Parkway NW, Unit 1010',
			    @param_add2=null,
			    @param_city='Kennesaw',
			    @param_state='GA',
			    @param_zip='30144',
			    @param_country='USA',
			    @param_lat='34.012',
			    @param_lon='-84.5618',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Kennesaw',
			    @param_email='CSC-25_Kennesaw@chickensaladchick.com',
			    @param_phone='678-290-0173',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='25.0',
			    @param_POSID=@posid;
		 




-- counting: 21 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='588 Pinnacle Place',
			    @param_add2=null,
			    @param_city='Prattville',
			    @param_state='AL',
			    @param_zip='36066',
			    @param_country='USA',
			    @param_lat='32.4639',
			    @param_lon='-86.398',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Prattville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-285-3729',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='27.0',
			    @param_POSID=@posid;
		 




-- counting: 22 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='214 Azalea Square Blvd Suite G',
			    @param_add2=null,
			    @param_city='Summerville',
			    @param_state='SC',
			    @param_zip='29483',
			    @param_country='USA',
			    @param_lat='33.0374',
			    @param_lon='-80.1609',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Summerville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='843-832-6968',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='29.0',
			    @param_POSID=@posid;
		 




-- counting: 23 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='101 South Tryon Street, Ste 10/11',
			    @param_add2=null,
			    @param_city='Charlotte',
			    @param_state='NC',
			    @param_zip='28280',
			    @param_country='USA',
			    @param_lat='35.2264',
			    @param_lon='-80.8427',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Charlotte - Bank of America Plaza',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='980-237-6873',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='28.0',
			    @param_POSID=@posid;
		 




-- counting: 24 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1830 29th Avenue South',
			    @param_add2=null,
			    @param_city='Homewood',
			    @param_state='AL',
			    @param_zip='35209',
			    @param_country='USA',
			    @param_lat='33.479929999999996',
			    @param_lon='-86.79013',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Birmingham - Homewood',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='205-637-5578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='26.0',
			    @param_POSID=@posid;
		 




-- counting: 25 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1105 Woodstock Rd. Suite 110',
			    @param_add2=null,
			    @param_city='Roswell',
			    @param_state='GA',
			    @param_zip='30075',
			    @param_country='USA',
			    @param_lat='34.0631',
			    @param_lon='-84.3962',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Roswell',
			    @param_email='CSC-31_Roswell@chickensaladchick.com',
			    @param_phone='770-998-0621',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='31.0',
			    @param_POSID=@posid;
		 




-- counting: 26 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='10920 Baymeadows Rd, Unit 12',
			    @param_add2=null,
			    @param_city='Jacksonville',
			    @param_state='FL',
			    @param_zip='32256',
			    @param_country='USA',
			    @param_lat='30.214000000000002',
			    @param_lon='-81.518',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Jacksonville - Baymeadows',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(904) 503-3304',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='36.0',
			    @param_POSID=@posid;
		 




-- counting: 27 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3604 Pelham Road Building D',
			    @param_add2=null,
			    @param_city='Greenville',
			    @param_state='SC',
			    @param_zip='29650',
			    @param_country='USA',
			    @param_lat='34.8603',
			    @param_lon='-82.2702',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Greenville #2',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(864) 603-3600',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='33.0',
			    @param_POSID=@posid;
		 




-- counting: 28 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1113 U.S. Highway 231',
			    @param_add2=null,
			    @param_city='Troy',
			    @param_state='AL',
			    @param_zip='36081',
			    @param_country='USA',
			    @param_lat='31.783620000000003',
			    @param_lon='-85.95966999999999',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Troy',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-770-0545',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='32.0',
			    @param_POSID=@posid;
		 




-- counting: 29 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1496 Apalachee Parkway, Unit 14',
			    @param_add2=null,
			    @param_city='Tallahassee',
			    @param_state='FL',
			    @param_zip='32301',
			    @param_country='USA',
			    @param_lat='30.436259999999997',
			    @param_lon='-84.25832',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tallahassee - Apalachee',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='850-402-0653',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='34.0',
			    @param_POSID=@posid;
		 




-- counting: 30 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1802 US Highway 98, Suite F',
			    @param_add2=null,
			    @param_city='Daphne',
			    @param_state='AL',
			    @param_zip='36526',
			    @param_country='USA',
			    @param_lat='30.6049',
			    @param_lon='-87.8967',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Daphne',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(251) 625-1092',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='37.0',
			    @param_POSID=@posid;
		 




-- counting: 31 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2118 Seventh Ave South',
			    @param_add2=null,
			    @param_city='Birmingham',
			    @param_state='AL',
			    @param_zip='35233',
			    @param_country='USA',
			    @param_lat='33.50713',
			    @param_lon='-86.79782',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Birmingham-Southside',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='2057030601',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='35.0',
			    @param_POSID=@posid;
		 




-- counting: 32 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='155 Traders Way Suite 300',
			    @param_add2=null,
			    @param_city='Pooler',
			    @param_state='GA',
			    @param_zip='31406',
			    @param_country='USA',
			    @param_lat='32.1393',
			    @param_lon='-81.2539',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Pooler',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='912-348-3389',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='39.0',
			    @param_POSID=@posid;
		 




-- counting: 33 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1310 Westover Terrace, Suite 107',
			    @param_add2=null,
			    @param_city='Greensboro',
			    @param_state='NC',
			    @param_zip='27408',
			    @param_country='USA',
			    @param_lat='36.09024',
			    @param_lon='-79.81314',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Greensboro',
			    @param_email='csc-38_greensboro@chickensaladchick.com',
			    @param_phone='(336) 663-8588',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='38.0',
			    @param_POSID=@posid;
		 




-- counting: 34 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2790 East Fowler AvenueSuite 490',
			    @param_add2=null,
			    @param_city='Tampa',
			    @param_state='FL',
			    @param_zip='33612',
			    @param_country='USA',
			    @param_lat='28.0546',
			    @param_lon='-82.4273',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tampa',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='8139104300',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='41.0',
			    @param_POSID=@posid;
		 




-- counting: 35 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='12101 University BlvdSuite 201',
			    @param_add2=null,
			    @param_city='Orlando',
			    @param_state='FL',
			    @param_zip='32817',
			    @param_country='USA',
			    @param_lat='28.5993',
			    @param_lon='-81.209',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Orlando',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(407) 867-4900',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='66.0',
			    @param_POSID=@posid;
		 




-- counting: 36 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4 S Tunnel Road',
			    @param_add2=null,
			    @param_city='Asheville',
			    @param_state='NC',
			    @param_zip='28805',
			    @param_country='USA',
			    @param_lat='35.5828',
			    @param_lon='-82.525',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Asheville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(828) 412-3466',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='43.0',
			    @param_POSID=@posid;
		 




-- counting: 37 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='75 N Nova Rd',
			    @param_add2=null,
			    @param_city='Ormond Beach',
			    @param_state='FL',
			    @param_zip='32174',
			    @param_country='USA',
			    @param_lat='29.28047',
			    @param_lon='-81.08196',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Ormond Beach',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='3866712160',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='42.0',
			    @param_POSID=@posid;
		 




-- counting: 38 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3045 SW 34th Street, Suite 16',
			    @param_add2=null,
			    @param_city='Gainesville',
			    @param_state='FL',
			    @param_zip='32608',
			    @param_country='USA',
			    @param_lat='29.6255',
			    @param_lon='-82.3705',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Gainesville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='3523753418',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='69.0',
			    @param_POSID=@posid;
		 




-- counting: 39 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='5753 Old Shell Rd',
			    @param_add2=null,
			    @param_city='Mobile',
			    @param_state='AL',
			    @param_zip='36608',
			    @param_country='USA',
			    @param_lat='30.6882',
			    @param_lon='-88.1757',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Mobile (USA)',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='251-408-3236',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='45.0',
			    @param_POSID=@posid;
		 




-- counting: 40 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='996 Bichara Blvd.',
			    @param_add2=null,
			    @param_city='The Villages',
			    @param_state='FL',
			    @param_zip='32159',
			    @param_country='USA',
			    @param_lat='28.9401',
			    @param_lon='-81.9464',
			    @param_timezoneid='America/New_York',
			    @param_storeName='The Villages',
			    @param_email='csc-48_the_villages@chickensaladchick.com',
			    @param_phone='3527759379',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='48.0',
			    @param_POSID=@posid;
		 




-- counting: 41 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='280 West Coleman Blvd Ste. F & G',
			    @param_add2=null,
			    @param_city='Mount Pleasant',
			    @param_state='SC',
			    @param_zip='29646',
			    @param_country='USA',
			    @param_lat='32.7982',
			    @param_lon='-79.892',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Mt. Pleasant',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='724-493-8030',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='50.0',
			    @param_POSID=@posid;
		 




-- counting: 42 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4624 Town Crossing Dr. #115',
			    @param_add2=null,
			    @param_city='Jacksonville',
			    @param_state='FL',
			    @param_zip='32246',
			    @param_country='USA',
			    @param_lat='30.2594',
			    @param_lon='-81.5277',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Jacksonville - St. Johns Town Center',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='904-438-5427',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='52.0',
			    @param_POSID=@posid;
		 




-- counting: 43 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1120 Coolidge Street, Suite A',
			    @param_add2=null,
			    @param_city='Lafayette',
			    @param_state='La',
			    @param_zip='70503',
			    @param_country='USA',
			    @param_lat='30.2043',
			    @param_lon='-92.0178',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Lafayette - Oil Center',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(337) 706-7471',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='46.0',
			    @param_POSID=@posid;
		 




-- counting: 44 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1003 Peachtree Parkway',
			    @param_add2=null,
			    @param_city='Peachtree City',
			    @param_state='GA',
			    @param_zip='30269',
			    @param_country='USA',
			    @param_lat='33.4408',
			    @param_lon='-84.5868',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Peachtree City',
			    @param_email='CSC-51_Peachtree@chickensaladchick.com',
			    @param_phone='(470) 878-5170',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='51.0',
			    @param_POSID=@posid;
		 




-- counting: 45 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2871 Washington Rd',
			    @param_add2=null,
			    @param_city='Augusta',
			    @param_state='GA',
			    @param_zip='30909',
			    @param_country='USA',
			    @param_lat='33.5107',
			    @param_lon='-82.0307',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Augusta',
			    @param_email='CSC-57_Augusta@chickensaladchick.com',
			    @param_phone='706-729-6556',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='57.0',
			    @param_POSID=@posid;
		 




-- counting: 46 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='15 Garlington Rd Suite 100',
			    @param_add2=null,
			    @param_city='Greenville',
			    @param_state='SC',
			    @param_zip='29615',
			    @param_country='USA',
			    @param_lat='34.8383',
			    @param_lon='-82.2798',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Greenville Garlington',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(864) 603-3737',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='56.0',
			    @param_POSID=@posid;
		 




-- counting: 47 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='11180 Tamiami Trail N',
			    @param_add2=null,
			    @param_city='Naples',
			    @param_state='FL',
			    @param_zip='34110',
			    @param_country='USA',
			    @param_lat='26.2735',
			    @param_lon='-81.8015',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Naples',
			    @param_email='chickensaladchicknaples@gmail.com',
			    @param_phone='239-431-5678',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='49.0',
			    @param_POSID=@posid;
		 




-- counting: 48 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='8825 Tehama Ridge Pkwy Ste 329',
			    @param_add2=null,
			    @param_city='Fort Worth',
			    @param_state='TX',
			    @param_zip='76177',
			    @param_country='USA',
			    @param_lat='32.8999',
			    @param_lon='-97.3228',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Ft. Worth',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='817-857-8501',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='55.0',
			    @param_POSID=@posid;
		 




-- counting: 49 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6025 Butler Point Rd',
			    @param_add2=null,
			    @param_city='JACKSONVILLE',
			    @param_state='FL',
			    @param_zip='32256',
			    @param_country='USA',
			    @param_lat='30.243570000000002',
			    @param_lon='-81.59834000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Jacksonville - Galleria',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='9046831447',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='53.0',
			    @param_POSID=@posid;
		 




-- counting: 50 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1305 Merchants Dr.',
			    @param_add2=null,
			    @param_city='Oxford',
			    @param_state='MS',
			    @param_zip='38655',
			    @param_country='USA',
			    @param_lat='34.36356',
			    @param_lon='-89.6365',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Oxford, MS',
			    @param_email='csc.oxford@gmail.com',
			    @param_phone='(662) 380-5582',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='72.0',
			    @param_POSID=@posid;
		 




-- counting: 51 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='11587 Regency Village Drive',
			    @param_add2=null,
			    @param_city='Orlando',
			    @param_state='FL',
			    @param_zip='32821',
			    @param_country='USA',
			    @param_lat='28.393309999999996',
			    @param_lon='-81.48874',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Orlando - Vineland Pointe',
			    @param_email='csc-112_vineland_pointe@chickensaladchick.com',
			    @param_phone='407-499-0981',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='112.0',
			    @param_POSID=@posid;
		 




-- counting: 52 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1765 Hwy 27 South',
			    @param_add2=null,
			    @param_city='Carrollton',
			    @param_state='GA',
			    @param_zip='30117',
			    @param_country='USA',
			    @param_lat='33.54265',
			    @param_lon='-85.07444',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Duplicate Store',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='6786640555',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='nan',
			    @param_POSID=@posid;
		 




-- counting: 53 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7350 Cortez Rd. W',
			    @param_add2=null,
			    @param_city='Bradenton',
			    @param_state='Fl',
			    @param_zip='34210',
			    @param_country='USA',
			    @param_lat='27.46347',
			    @param_lon='-82.63493000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Bradenton',
			    @param_email='info@chickensaladchick.com',
			    @param_phone='941-761-4440',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='nan',
			    @param_POSID=@posid;
		 




-- counting: 54 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7917 Beechmont Ave',
			    @param_add2=null,
			    @param_city='Cincinnati ',
			    @param_state='OH',
			    @param_zip='45255',
			    @param_country='USA',
			    @param_lat='39.07228',
			    @param_lon='-84.33878',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Anderson Township, OH',
			    @param_email='csc-154_anderson@chickensaladchick.com',
			    @param_phone='513-388-9111',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='154.0',
			    @param_POSID=@posid;
		 




-- counting: 55 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6124 Camp Bowie Blvd',
			    @param_add2=null,
			    @param_city='Ft. Worth',
			    @param_state='TX',
			    @param_zip='76116',
			    @param_country='USA',
			    @param_lat='32.72913',
			    @param_lon='-97.41604',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Ft. Worth - Ridglea ',
			    @param_email='csc-155_ridglea@chickensaladchick.com',
			    @param_phone='817-857-8507',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='155.0',
			    @param_POSID=@posid;
		 




-- counting: 56 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='196 Alps Rd Beechwood Promenade',
			    @param_add2=null,
			    @param_city='Athens',
			    @param_state='GA',
			    @param_zip='30606',
			    @param_country='USA',
			    @param_lat='33.944320000000005',
			    @param_lon='-83.4092',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Athens',
			    @param_email='CSC-58_Athens@chickensaladchick.com',
			    @param_phone='706-549-7580',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='58.0',
			    @param_POSID=@posid;
		 




-- counting: 57 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7614 Hwy 70 S Ste. 606',
			    @param_add2=null,
			    @param_city='Nashville',
			    @param_state='TN',
			    @param_zip='37221',
			    @param_country='USA',
			    @param_lat='36.078959999999995',
			    @param_lon='-86.9501',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Bellevue - Nashville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='615-645-9883',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='70.0',
			    @param_POSID=@posid;
		 




-- counting: 58 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1720 Old Fannin Rd. ',
			    @param_add2=null,
			    @param_city='Flowood',
			    @param_state='MS',
			    @param_zip='39232',
			    @param_country='USA',
			    @param_lat='32.343140000000005',
			    @param_lon='-90.06472',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Flowood',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='769-257-7092',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='69.0',
			    @param_POSID=@posid;
		 




-- counting: 59 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='40 25th STREET',
			    @param_add2=null,
			    @param_city='Pittsburgh',
			    @param_state='PA',
			    @param_zip='15222',
			    @param_country='USA',
			    @param_lat='40.44753',
			    @param_lon='-79.9934',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Test Store',
			    @param_email='pitt@sessionm.com',
			    @param_phone='0123456789',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='5.0',
			    @param_POSID=@posid;
		 




-- counting: 60 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='17623 Dale Mabry Highway',
			    @param_add2=null,
			    @param_city='Lutz',
			    @param_state='FL',
			    @param_zip='33548',
			    @param_country='USA',
			    @param_lat='28.125290000000003',
			    @param_lon='-82.50293',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Lutz, FL',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='813-488-1575',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='98.0',
			    @param_POSID=@posid;
		 




-- counting: 61 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2126 Exeter Rd',
			    @param_add2=null,
			    @param_city='Germantown',
			    @param_state='TN',
			    @param_zip='38138',
			    @param_country='USA',
			    @param_lat='35.091120000000004',
			    @param_lon='-89.80244',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Germantown, TN',
			    @param_email='csc-96_germantown@chickensaladchick.com',
			    @param_phone='(901) 308-0487',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='96.0',
			    @param_POSID=@posid;
		 




-- counting: 62 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='946 W Mitchell Hammock Road ',
			    @param_add2=null,
			    @param_city='Oviedo',
			    @param_state='FL',
			    @param_zip='32765',
			    @param_country='USA',
			    @param_lat='28.655170000000002',
			    @param_lon='-81.22303000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Oviedo, FL',
			    @param_email='csc-99_oviedo@chickensaladchick.com',
			    @param_phone='3342754578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='99.0',
			    @param_POSID=@posid;
		 




-- counting: 63 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='600 Jefferson St',
			    @param_add2=null,
			    @param_city='Lafayette',
			    @param_state='LA',
			    @param_zip='70501',
			    @param_country='USA',
			    @param_lat='30.2234',
			    @param_lon='-92.02135',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Lafayette - Chase Tower',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='337-266-2325',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='8046.0',
			    @param_POSID=@posid;
		 




-- counting: 64 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='800 Martha Berry Blvd NE',
			    @param_add2=null,
			    @param_city='Rome',
			    @param_state='GA',
			    @param_zip='30165',
			    @param_country='USA',
			    @param_lat='34.261720000000004',
			    @param_lon='-85.18047',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Rome, GA - STACY''S CHICK',
			    @param_email='csc-124_rome@chickensaladchick.com',
			    @param_phone='706-528-4929',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='124.0',
			    @param_POSID=@posid;
		 




-- counting: 65 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='10343 E. HWY 30A',
			    @param_add2=null,
			    @param_city='Santa Rosa Beach',
			    @param_state='FL',
			    @param_zip='32413',
			    @param_country='USA',
			    @param_lat='30.28133',
			    @param_lon='-86.01909',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Santa Rosa Beach',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(850) 233-3134',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='35.0',
			    @param_POSID=@posid;
		 




-- counting: 66 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='726 Watkins Road',
			    @param_add2=null,
			    @param_city='Maryville',
			    @param_state='TN',
			    @param_zip='37801',
			    @param_country='USA',
			    @param_lat='35.75117',
			    @param_lon='-83.99294',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Maryville, TN',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(865) 357-1587',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='101.0',
			    @param_POSID=@posid;
		 




-- counting: 67 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1131 A Military Cutoff Road',
			    @param_add2=null,
			    @param_city='Wilmington',
			    @param_state='NC',
			    @param_zip='28405',
			    @param_country='USA',
			    @param_lat='34.23482',
			    @param_lon='-77.82812',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Wilmington, NC',
			    @param_email='csc-153_wilmington@chickensaladchick.com',
			    @param_phone='(910) 679-8126',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='153.0',
			    @param_POSID=@posid;
		 




-- counting: 68 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2416 Dawson Rd. #1',
			    @param_add2=null,
			    @param_city='Albany',
			    @param_state='GA',
			    @param_zip='31707',
			    @param_country='USA',
			    @param_lat='31.60945',
			    @param_lon='-84.21056999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Albany',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(229) 255-3366',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='91.0',
			    @param_POSID=@posid;
		 




-- counting: 69 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='20 Discovery Drive',
			    @param_add2=null,
			    @param_city='Bluffton',
			    @param_state='SC',
			    @param_zip='29910',
			    @param_country='USA',
			    @param_lat='32.27258',
			    @param_lon='-80.91608000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Bluffton, SC',
			    @param_email='csc-163_bluffton@chickensaladchick.com',
			    @param_phone='843-949-4030',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='163.0',
			    @param_POSID=@posid;
		 




-- counting: 70 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='975 E 3rd Street Suite 122',
			    @param_add2=null,
			    @param_city='Chattanooga',
			    @param_state='TN',
			    @param_zip='37403',
			    @param_country='USA',
			    @param_lat='35.04902',
			    @param_lon='-85.29274000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Chattanooga - Erlanger Medical Mall',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-275-4578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='8016.0',
			    @param_POSID=@posid;
		 




-- counting: 71 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2404 E 2nd Street Edmond',
			    @param_add2=null,
			    @param_city='Edmond',
			    @param_state='OK',
			    @param_zip='73034',
			    @param_country='USA',
			    @param_lat='35.65229',
			    @param_lon='-97.4488',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Edmond, OK',
			    @param_email='csc-125_edmond@chickensaladchick.com',
			    @param_phone='(405) 920-6063',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='125.0',
			    @param_POSID=@posid;
		 




-- counting: 72 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1001 Eagles Landing Parkway',
			    @param_add2=null,
			    @param_city='Stockbridge',
			    @param_state='GA',
			    @param_zip='30281',
			    @param_country='USA',
			    @param_lat='33.51023',
			    @param_lon='-84.2259',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Stockbridge, GA',
			    @param_email='csc-140_stockbridge@chickensaladchick.com',
			    @param_phone='678-782-7216',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='140.0',
			    @param_POSID=@posid;
		 




-- counting: 73 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='21788 Katy Freeway',
			    @param_add2=null,
			    @param_city='Katy',
			    @param_state='TX',
			    @param_zip='77449',
			    @param_country='USA',
			    @param_lat='29.786459999999998',
			    @param_lon='-95.74768',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Katy, TX',
			    @param_email='csc-133_katy@chickensaladchick.com',
			    @param_phone='(832) 391-6647',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='133.0',
			    @param_POSID=@posid;
		 




-- counting: 74 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3002 Hardy St. ',
			    @param_add2=null,
			    @param_city='Hattiesburg',
			    @param_state='MS',
			    @param_zip='39401',
			    @param_country='USA',
			    @param_lat='31.324270000000002',
			    @param_lon='-89.33482',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Hattiesburg, MS ',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(769) 390-7050',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='76.0',
			    @param_POSID=@posid;
		 




-- counting: 75 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2323 Plum Street',
			    @param_add2=null,
			    @param_city='Edwardsville',
			    @param_state='IL',
			    @param_zip='62025',
			    @param_country='USA',
			    @param_lat='38.78512',
			    @param_lon='-89.95926999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Edwardsville, IL',
			    @param_email='csc-131_edwardsville@chickensaladchick.com',
			    @param_phone='(618) 238-2839',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='131.0',
			    @param_POSID=@posid;
		 




-- counting: 76 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2810 Paces Ferry Road Ste 310',
			    @param_add2=null,
			    @param_city='Atlanta',
			    @param_state='GA',
			    @param_zip='30339',
			    @param_country='USA',
			    @param_lat='33.86589',
			    @param_lon='-84.47163',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Vinings',
			    @param_email='CSC-92_Vinings@chickensaladchick.com',
			    @param_phone='678-247-8541',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='92.0',
			    @param_POSID=@posid;
		 




-- counting: 77 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7709 Highway 72 West Suite 100',
			    @param_add2=null,
			    @param_city='Madison',
			    @param_state='AL',
			    @param_zip='35758',
			    @param_country='USA',
			    @param_lat='34.75417',
			    @param_lon='-86.7374',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Madison',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(256) 325-1041',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='67.0',
			    @param_POSID=@posid;
		 




-- counting: 78 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='214 Newnan Crossing Bypass',
			    @param_add2=null,
			    @param_city='Newnan',
			    @param_state='GA',
			    @param_zip='30265',
			    @param_country='USA',
			    @param_lat='33.39145',
			    @param_lon='-84.7629',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Newnan ',
			    @param_email='CSC-74_Newnan@chickensaladchick.com',
			    @param_phone='770-683-2696',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='74.0',
			    @param_POSID=@posid;
		 




-- counting: 79 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='12096 State Rd 54',
			    @param_add2=null,
			    @param_city='Odessa',
			    @param_state='FL',
			    @param_zip='33556',
			    @param_country='USA',
			    @param_lat='28.18988',
			    @param_lon='-82.61584',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Trinity, FL',
			    @param_email='csc-149_trinity@chickensaladchick.com',
			    @param_phone='727.685.3888',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='149.0',
			    @param_POSID=@posid;
		 




-- counting: 80 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1765 Hwy 27 South',
			    @param_add2=null,
			    @param_city='Carrollton',
			    @param_state='GA',
			    @param_zip='30117',
			    @param_country='USA',
			    @param_lat='33.54265',
			    @param_lon='-85.07444',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Carrollton, GA',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='6786640555',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='102.0',
			    @param_POSID=@posid;
		 




-- counting: 81 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='27306 Crossing Circle Suite 270',
			    @param_add2=null,
			    @param_city='Denham Springs',
			    @param_state='LA',
			    @param_zip='70726',
			    @param_country='USA',
			    @param_lat='30.467059999999996',
			    @param_lon='-90.91927',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Denham Springs',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='225-243-7524',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='80.0',
			    @param_POSID=@posid;
		 




-- counting: 82 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='724 North Dean Rd',
			    @param_add2=null,
			    @param_city='Auburn',
			    @param_state='AL',
			    @param_zip='36830',
			    @param_country='USA',
			    @param_lat='32.6211',
			    @param_lon='-85.4616',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='AL018',
			    @param_email='ali.rauch@simplysouthernrg.com',
			    @param_phone='3342754578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='987.0',
			    @param_POSID=@posid;
		 




-- counting: 83 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4365 Roswell Rd NE',
			    @param_add2=null,
			    @param_city='Buckhead',
			    @param_state='GA',
			    @param_zip='30342',
			    @param_country='USA',
			    @param_lat='33.87376',
			    @param_lon='-84.38005',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Buckhead',
			    @param_email='CSC-78_Buckhead@chickensaladchick.com',
			    @param_phone='(678) 732-3573',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='78.0',
			    @param_POSID=@posid;
		 




-- counting: 84 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='10300 Louetta Road',
			    @param_add2=null,
			    @param_city='Houston',
			    @param_state='TX',
			    @param_zip='77070',
			    @param_country='USA',
			    @param_lat='29.99873',
			    @param_lon='-95.56814',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Houston - Vintage Park',
			    @param_email='csc-130_vintage_park@chickensaladchick.com',
			    @param_phone='(346) 808-5971',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='130.0',
			    @param_POSID=@posid;
		 




-- counting: 85 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1122 Dawsonville Hwy, Suite 500',
			    @param_add2=null,
			    @param_city='Gainesville',
			    @param_state='GA',
			    @param_zip='30501',
			    @param_country='USA',
			    @param_lat='34.30235',
			    @param_lon='-83.85825',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Gainesville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(678) 971-1640',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='75.0',
			    @param_POSID=@posid;
		 




-- counting: 86 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4867 Main Street',
			    @param_add2=null,
			    @param_city='Spring Hill',
			    @param_state='TN',
			    @param_zip='37174',
			    @param_country='USA',
			    @param_lat='35.77854',
			    @param_lon='-86.91537',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Spring Hill, TN',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(615) 392-8555',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='88.0',
			    @param_POSID=@posid;
		 




-- counting: 87 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7839A 113th Street',
			    @param_add2=null,
			    @param_city='North Seminole',
			    @param_state='FL',
			    @param_zip='33772',
			    @param_country='USA',
			    @param_lat='27.84242',
			    @param_lon='-82.7974',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Seminole',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(727) 319-2905',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='89.0',
			    @param_POSID=@posid;
		 




-- counting: 88 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='906 Boll Weevil Circle',
			    @param_add2=null,
			    @param_city='Enterprise',
			    @param_state='AL',
			    @param_zip='36330',
			    @param_country='USA',
			    @param_lat='31.33495',
			    @param_lon='-85.85477',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Enterprise',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(334) 417-0096',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='79.0',
			    @param_POSID=@posid;
		 




-- counting: 89 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='7350 Cortez Rd W',
			    @param_add2=null,
			    @param_city='Bradenton',
			    @param_state='FL',
			    @param_zip='34210',
			    @param_country='USA',
			    @param_lat='27.46347',
			    @param_lon='-82.63493000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Bradenton',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='9417614440',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='60.0',
			    @param_POSID=@posid;
		 




-- counting: 90 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='217 Indian Lake Blvd.',
			    @param_add2=null,
			    @param_city='Hendersonville',
			    @param_state='TN',
			    @param_zip='37075',
			    @param_country='USA',
			    @param_lat='36.321490000000004',
			    @param_lon='-86.60159',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Hendersonville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='615-447-3006',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='65.0',
			    @param_POSID=@posid;
		 




-- counting: 91 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='17215 Chesterfield Airport Rd',
			    @param_add2=null,
			    @param_city='Chesterfield',
			    @param_state='MO',
			    @param_zip='63005',
			    @param_country='USA',
			    @param_lat='38.669059999999995',
			    @param_lon='-90.59804',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Chesterfield, MO',
			    @param_email='csc-121_chesterfield@chickensaladchick.com',
			    @param_phone='(636) 778-9452',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='121.0',
			    @param_POSID=@posid;
		 




-- counting: 92 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='9631 W Broad Street',
			    @param_add2=null,
			    @param_city='Glen Allen',
			    @param_state='VA',
			    @param_zip='23060',
			    @param_country='USA',
			    @param_lat='37.63986',
			    @param_lon='-77.56491',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Richmond, VA (Westpark)',
			    @param_email='csc-157_richmond@chickensaladchick.com',
			    @param_phone='804-912-1630',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='157.0',
			    @param_POSID=@posid;
		 




-- counting: 93 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='8915 Christenbury Parkway Suite 40',
			    @param_add2=null,
			    @param_city='Concord',
			    @param_state='NC',
			    @param_zip='28027',
			    @param_country='USA',
			    @param_lat='35.38015',
			    @param_lon='-80.72733000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Concord, NC',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='7049517323',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='77.0',
			    @param_POSID=@posid;
		 




-- counting: 94 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6535 Youree Drive',
			    @param_add2=null,
			    @param_city='Shreveport',
			    @param_state='LA',
			    @param_zip='71105',
			    @param_country='USA',
			    @param_lat='32.4473',
			    @param_lon='-93.71941',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Shreveport',
			    @param_email='CSC-66_Shreveport@chickensaladchick.com',
			    @param_phone='(318) 524-9960',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='66.0',
			    @param_POSID=@posid;
		 




-- counting: 95 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='724 North Dean Rd',
			    @param_add2=null,
			    @param_city='Auburn',
			    @param_state='AL',
			    @param_zip='36830',
			    @param_country='USA',
			    @param_lat='32.6211',
			    @param_lon='-85.4616',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='CSC NCR Silver Lab',
			    @param_email='info@chickensaladchick.com',
			    @param_phone='334-275-4578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='999.0',
			    @param_POSID=@posid;
		 




-- counting: 96 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='449 E Main Street',
			    @param_add2=null,
			    @param_city='Spartanburg',
			    @param_state='SC',
			    @param_zip='29302',
			    @param_country='USA',
			    @param_lat='34.952059999999996',
			    @param_lon='-81.92008',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Spartanburg, SC',
			    @param_email='csc-151_spartanburg@chickensaladchick.com',
			    @param_phone='864-205-2812',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='151.0',
			    @param_POSID=@posid;
		 




-- counting: 97 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3520 W University Dr',
			    @param_add2=null,
			    @param_city='McKinney',
			    @param_state='TX',
			    @param_zip='75071',
			    @param_country='USA',
			    @param_lat='33.218090000000004',
			    @param_lon='-96.69402',
			    @param_timezoneid='America/New_York',
			    @param_storeName='McKinney, TX',
			    @param_email='csc-115_mckinney@chickensaladchick.com',
			    @param_phone='(214) 856-3908',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='115.0',
			    @param_POSID=@posid;
		 




-- counting: 98 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2012 Rainbow Drive',
			    @param_add2=null,
			    @param_city='Gadsden',
			    @param_state='AL',
			    @param_zip='35901',
			    @param_country='USA',
			    @param_lat='33.973890000000004',
			    @param_lon='-86.0155',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Gadsden',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(256) 952-2625',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='82.0',
			    @param_POSID=@posid;
		 




-- counting: 99 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='352 East Joyce Blvd',
			    @param_add2=null,
			    @param_city='Fayetteville',
			    @param_state='AR',
			    @param_zip='72703',
			    @param_country='USA',
			    @param_lat='36.12465',
			    @param_lon='-94.15334',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Fayetteville, AR',
			    @param_email='csc-141_fayetteville@chickensaladchick.com',
			    @param_phone='(479) 301-2332',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='141.0',
			    @param_POSID=@posid;
		 




-- counting: 100 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3803 Highway 22',
			    @param_add2=null,
			    @param_city='Mandeville',
			    @param_state='LA',
			    @param_zip='70421',
			    @param_country='USA',
			    @param_lat='30.394740000000002',
			    @param_lon='-90.09105',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Mandeville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(985) 778-2670',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='68.0',
			    @param_POSID=@posid;
		 




-- counting: 101 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2233 Matthews Township Parkway',
			    @param_add2=null,
			    @param_city='Matthews',
			    @param_state='NC',
			    @param_zip='28105',
			    @param_country='USA',
			    @param_lat='35.128029999999995',
			    @param_lon='-80.70465',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Matthews, NC',
			    @param_email='csc-148_matthews@chickensaladchick.com',
			    @param_phone='980-339-7700',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='148.0',
			    @param_POSID=@posid;
		 




-- counting: 102 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='254 E Brannon Rd',
			    @param_add2=null,
			    @param_city='Nicholasville',
			    @param_state='KY',
			    @param_zip='40356',
			    @param_country='USA',
			    @param_lat='37.95627',
			    @param_lon='-84.53957',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Nicholasville/Lexington, KY',
			    @param_email='csc-116_nicholasville@chickensaladchick.com',
			    @param_phone='(859) 273 4000',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='116.0',
			    @param_POSID=@posid;
		 




-- counting: 103 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='501 Carroll Street',
			    @param_add2=null,
			    @param_city='TX',
			    @param_state='TX',
			    @param_zip='76107',
			    @param_country='USA',
			    @param_lat='32.753170000000004',
			    @param_lon='-97.35439000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Ft. Worth, TX (Montgomery Plaza)',
			    @param_email='csc-168_montplaza@chickensaladchick.com',
			    @param_phone='817-857-8509',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='168.0',
			    @param_POSID=@posid;
		 




-- counting: 104 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='30129 Rock Creek Drive',
			    @param_add2=null,
			    @param_city='Kingwood',
			    @param_state='TX',
			    @param_zip='77339',
			    @param_country='USA',
			    @param_lat='30.069879999999998',
			    @param_lon='-95.2494',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Houston - Kingwood',
			    @param_email='csc-139_north_park@chickensaladchick.com',
			    @param_phone='281-623-5739',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='139.0',
			    @param_POSID=@posid;
		 




-- counting: 105 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4562 Poplar Avenue',
			    @param_add2=null,
			    @param_city='Memphis',
			    @param_state='TN',
			    @param_zip='38117',
			    @param_country='USA',
			    @param_lat='35.11758',
			    @param_lon='-89.91016',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Memphis, TN - Poplar Perkins',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-275-4578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='95.0',
			    @param_POSID=@posid;
		 




-- counting: 106 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1024 MacArthur Dr.',
			    @param_add2=null,
			    @param_city='Alexandria',
			    @param_state='LA',
			    @param_zip='71303',
			    @param_country='USA',
			    @param_lat='31.29125',
			    @param_lon='-92.4799',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Alexandria, LA',
			    @param_email='csc-152_alexandria@chickensaladchick.com',
			    @param_phone='318-545-4646',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='152.0',
			    @param_POSID=@posid;
		 




-- counting: 107 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='5050 Carothers Pkwy',
			    @param_add2=null,
			    @param_city='Franklin',
			    @param_state='TN',
			    @param_zip='37067',
			    @param_country='USA',
			    @param_lat='35.92575',
			    @param_lon='-86.81819',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Franklin, TN',
			    @param_email='csc-94_franklin@chickensaladchick.com',
			    @param_phone='615-628-8062',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='94.0',
			    @param_POSID=@posid;
		 




-- counting: 108 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='101 Saloom Farm Road',
			    @param_add2=null,
			    @param_city='Lafayette',
			    @param_state='LA',
			    @param_zip='70508',
			    @param_country='USA',
			    @param_lat='30.154740000000004',
			    @param_lon='-92.03712',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Lafayette Ambassador',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='337-983-2350',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='47.0',
			    @param_POSID=@posid;
		 




-- counting: 109 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1520 Veterans Parkway',
			    @param_add2=null,
			    @param_city='Jeffersonville',
			    @param_state='IN',
			    @param_zip='47130',
			    @param_country='USA',
			    @param_lat='38.32906',
			    @param_lon='-85.7477',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Jeffersonville, IN - COMING SOON!',
			    @param_email='csc-119_jeffersonville@chickensaladchick.com',
			    @param_phone='334-292-3611',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='119.0',
			    @param_POSID=@posid;
		 




-- counting: 110 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4050 W. Kennedy',
			    @param_add2=null,
			    @param_city='Tampa',
			    @param_state='FL',
			    @param_zip='33609',
			    @param_country='USA',
			    @param_lat='27.9444',
			    @param_lon='-82.51395',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tampa - South',
			    @param_email='csc-138_south_tampa@chickensaladchick.com',
			    @param_phone='(813) 515-5600',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='138.0',
			    @param_POSID=@posid;
		 




-- counting: 111 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1821 Beltline Drive Suite C',
			    @param_add2=null,
			    @param_city='Decatur',
			    @param_state='AL',
			    @param_zip='35601',
			    @param_country='USA',
			    @param_lat='34.57412',
			    @param_lon='-87.01890999999999',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Decatur',
			    @param_email='csc-84_decatur@chickensaladchick.com',
			    @param_phone='256-552-7500',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='84.0',
			    @param_POSID=@posid;
		 




-- counting: 112 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1676 Bass Road',
			    @param_add2=null,
			    @param_city='Macon',
			    @param_state='GA',
			    @param_zip='31210',
			    @param_country='USA',
			    @param_lat='32.932520000000004',
			    @param_lon='-83.72645',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Macon, GA',
			    @param_email='csc-164_macon@chickensaladchick.com',
			    @param_phone='478-259-4494',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='164.0',
			    @param_POSID=@posid;
		 




-- counting: 113 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3341 Regent Blvd',
			    @param_add2=null,
			    @param_city='Irving',
			    @param_state='TX',
			    @param_zip='75063',
			    @param_country='USA',
			    @param_lat='32.92125',
			    @param_lon='-96.9932',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Irving, TX',
			    @param_email='csc-126_irving@chickensaladchick.com',
			    @param_phone='(469) 677-0020',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='126.0',
			    @param_POSID=@posid;
		 




-- counting: 114 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6507 Old Brick Road',
			    @param_add2=null,
			    @param_city='Windermere',
			    @param_state='FL',
			    @param_zip='34786',
			    @param_country='USA',
			    @param_lat='28.45125',
			    @param_lon='-81.565',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Windermere, FL - COMING SOON!',
			    @param_email='CSC-143_Windermere@chickensaladchick.com',
			    @param_phone='334-292-3611',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='143.0',
			    @param_POSID=@posid;
		 




-- counting: 115 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4820 E. 61st Street',
			    @param_add2=null,
			    @param_city='Tulsa',
			    @param_state='OK',
			    @param_zip='74136',
			    @param_country='USA',
			    @param_lat='36.07521',
			    @param_lon='-95.92533',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tulsa - Warren Place',
			    @param_email='csc-112_warren_place@chickensaladchick.com',
			    @param_phone='539-867-1631',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='129.0',
			    @param_POSID=@posid;
		 




-- counting: 116 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1655 Hwy 20 West',
			    @param_add2=null,
			    @param_city='McDonough',
			    @param_state='GA',
			    @param_zip='30253',
			    @param_country='USA',
			    @param_lat='33.41891',
			    @param_lon='-84.19244',
			    @param_timezoneid='America/New_York',
			    @param_storeName='McDonough, GA',
			    @param_email='CSC-103_McDonough@chickensaladchick.com',
			    @param_phone='(678) 661-7717',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='103.0',
			    @param_POSID=@posid;
		 




-- counting: 117 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1265 Interstate Drive',
			    @param_add2=null,
			    @param_city='Cookeville',
			    @param_state='TN',
			    @param_zip='38501',
			    @param_country='USA',
			    @param_lat='36.13863',
			    @param_lon='-85.51054',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Cookeville, TN',
			    @param_email='csc-134_cookeville@chickensaladchick.com',
			    @param_phone='(931) 651-2530',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='134.0',
			    @param_POSID=@posid;
		 




-- counting: 118 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='200 North Dixie Avenue',
			    @param_add2=null,
			    @param_city='GA',
			    @param_state='GA',
			    @param_zip='30120',
			    @param_country='USA',
			    @param_lat='34.17242',
			    @param_lon='-84.78806',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Cartersville, GA',
			    @param_email='csc-175_cartersville@chickensaladchick.com',
			    @param_phone='(678) 719-0875',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='175.0',
			    @param_POSID=@posid;
		 




-- counting: 119 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='602 Hwy. 12',
			    @param_add2=null,
			    @param_city='Starkville',
			    @param_state='MS',
			    @param_zip='39759',
			    @param_country='USA',
			    @param_lat='33.45406',
			    @param_lon='-88.80962',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Starkville, MS',
			    @param_email='csc-110_starkville@chickensaladchick.com',
			    @param_phone='662-498-0120',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='110.0',
			    @param_POSID=@posid;
		 




-- counting: 120 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3821-G Promenade Pkwy',
			    @param_add2=null,
			    @param_city='D''iberville',
			    @param_state='MS',
			    @param_zip='39540',
			    @param_country='USA',
			    @param_lat='30.45627',
			    @param_lon='-88.90059000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='D''iberville, MS',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='228-280-8081',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='111.0',
			    @param_POSID=@posid;
		 




-- counting: 121 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='965 E Bloomingdale Avenue',
			    @param_add2=null,
			    @param_city='Brandon',
			    @param_state='FL',
			    @param_zip='33511',
			    @param_country='USA',
			    @param_lat='27.89306',
			    @param_lon='-82.27134000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Brandon, FL',
			    @param_email='csc-108_brandon@chickensaladchick.com',
			    @param_phone='813-654-0007',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='108.0',
			    @param_POSID=@posid;
		 




-- counting: 122 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3900 Arlington Highlands Blvd.',
			    @param_add2=null,
			    @param_city='Arlington',
			    @param_state='TX',
			    @param_zip='76018',
			    @param_country='USA',
			    @param_lat='32.681059999999995',
			    @param_lon='-97.11197',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Arlington, TX',
			    @param_email='csc-142_arlington@chickensaladchick.com',
			    @param_phone='682-410-0440',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='142.0',
			    @param_POSID=@posid;
		 




-- counting: 123 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2960 Shallowford Rd.',
			    @param_add2=null,
			    @param_city='Marietta',
			    @param_state='GA',
			    @param_zip='30066',
			    @param_country='USA',
			    @param_lat='34.03494',
			    @param_lon='-84.46897',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Sandy Plains, GA',
			    @param_email='csc-106_sandy_plains@chickensaladchick.com',
			    @param_phone='(770) 485-0920',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='106.0',
			    @param_POSID=@posid;
		 




-- counting: 124 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2855 Medical Center Parkway ,Suite F',
			    @param_add2=null,
			    @param_city='Murfreesboro',
			    @param_state='TN',
			    @param_zip='37129',
			    @param_country='USA',
			    @param_lat='35.86435',
			    @param_lon='-86.44636',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Murfreesboro',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='615-900-3087',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='64.0',
			    @param_POSID=@posid;
		 




-- counting: 125 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='5709 Calhoun Memorial Highway',
			    @param_add2=null,
			    @param_city='Easley',
			    @param_state='SC',
			    @param_zip='29642',
			    @param_country='USA',
			    @param_lat='34.82483',
			    @param_lon='-82.57113000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Easley, SC',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='864-442-5750',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='86.0',
			    @param_POSID=@posid;
		 




-- counting: 126 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='14030 FM 2920 Rd',
			    @param_add2=null,
			    @param_city='Tomball',
			    @param_state='TX',
			    @param_zip='77377',
			    @param_country='USA',
			    @param_lat='30.0906',
			    @param_lon='-95.63373',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tomball, TX',
			    @param_email='csc-161_tomball@chickensaladchick.com',
			    @param_phone='832-761-7858',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='161.0',
			    @param_POSID=@posid;
		 




-- counting: 127 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2821 Parkwood Rd',
			    @param_add2=null,
			    @param_city='Jonesboro',
			    @param_state='AR',
			    @param_zip='72401',
			    @param_country='USA',
			    @param_lat='35.81751',
			    @param_lon='-90.67175',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Jonesboro, AR',
			    @param_email='csc-100_jonesboro@chickensaladchick.com',
			    @param_phone='870-336-5678',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='100.0',
			    @param_POSID=@posid;
		 




-- counting: 128 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6575 Mechanicsville Turnpike',
			    @param_add2=null,
			    @param_city='Mechanicsville',
			    @param_state='VA',
			    @param_zip='23111',
			    @param_country='USA',
			    @param_lat='37.61258',
			    @param_lon='-77.33783000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Richmond, VA - Mechanicsville - COMING SOON!',
			    @param_email='csc-169_mechanicsville@chickensaladchick.com',
			    @param_phone='334-292-3611',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='169.0',
			    @param_POSID=@posid;
		 




-- counting: 129 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='11655 FM 2154',
			    @param_add2=null,
			    @param_city='College Station',
			    @param_state='TX',
			    @param_zip='77845',
			    @param_country='USA',
			    @param_lat='30.585040000000003',
			    @param_lon='-96.32852',
			    @param_timezoneid='America/New_York',
			    @param_storeName='College Station, TX',
			    @param_email='csc-137_college_station@chickensaladchick.com',
			    @param_phone='979-704-5209',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='137.0',
			    @param_POSID=@posid;
		 




-- counting: 130 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3581 N Gloster St',
			    @param_add2=null,
			    @param_city='Tupelo',
			    @param_state='MS',
			    @param_zip='38804',
			    @param_country='USA',
			    @param_lat='34.30458',
			    @param_lon='-88.71037',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tupelo, MS ',
			    @param_email='csc-118_tupelo@chickensaladchick.com',
			    @param_phone='662-269-3265',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='118.0',
			    @param_POSID=@posid;
		 




-- counting: 131 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='9470 Narcoosee Road',
			    @param_add2=null,
			    @param_city='Orlando',
			    @param_state='FL',
			    @param_zip='32827',
			    @param_country='USA',
			    @param_lat='28.429440000000003',
			    @param_lon='-81.25671',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Lake Nona',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='407-271-8236',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='63.0',
			    @param_POSID=@posid;
		 




-- counting: 132 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1000-9 S. Ponce de Leon Blvd.',
			    @param_add2=null,
			    @param_city='St. Augustine',
			    @param_state='FL',
			    @param_zip='32084',
			    @param_country='USA',
			    @param_lat='29.88055',
			    @param_lon='-81.32781999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='St. Augustine, FL ',
			    @param_email='csc-135_st_augustine@chickensaladchick.com',
			    @param_phone='(904) 547-2369',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='135.0',
			    @param_POSID=@posid;
		 




-- counting: 133 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='250 Paul Huff Pkwy NW',
			    @param_add2=null,
			    @param_city='Cleveland',
			    @param_state='TN',
			    @param_zip='37312',
			    @param_country='USA',
			    @param_lat='35.20602',
			    @param_lon='-84.84888000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Cleveland, TN',
			    @param_email='csc-160_cleveland_tn@chickensaladchick.com',
			    @param_phone='(423) 790-0570',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='160.0',
			    @param_POSID=@posid;
		 




-- counting: 134 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='35271 US Hwy 19 N',
			    @param_add2=null,
			    @param_city='Palm Harbor',
			    @param_state='FL',
			    @param_zip='34684',
			    @param_country='USA',
			    @param_lat='28.09277',
			    @param_lon='-82.73855999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Palm Harbor',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(727) 754-8185',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='61.0',
			    @param_POSID=@posid;
		 




-- counting: 135 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1128 Vann Dr.',
			    @param_add2=null,
			    @param_city='Jackson',
			    @param_state='TN',
			    @param_zip='38305',
			    @param_country='USA',
			    @param_lat='35.666270000000004',
			    @param_lon='-88.85821999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Jackson',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='7313004506',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='71.0',
			    @param_POSID=@posid;
		 




-- counting: 136 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1191 Lamy Lane',
			    @param_add2=null,
			    @param_city='Monroe',
			    @param_state='LA',
			    @param_zip='71201',
			    @param_country='USA',
			    @param_lat='32.52572',
			    @param_lon='-92.09746',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Monroe, LA ',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(318) 322-4425',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='97.0',
			    @param_POSID=@posid;
		 




-- counting: 137 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1320 E Hillside Drive',
			    @param_add2=null,
			    @param_city='Broken Arrow',
			    @param_state='OK',
			    @param_zip='74012',
			    @param_country='USA',
			    @param_lat='36.065290000000005',
			    @param_lon='-95.77488000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Broken Arrow, OK',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='918-505-5850',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='104.0',
			    @param_POSID=@posid;
		 




-- counting: 138 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='205 Government St.',
			    @param_add2=null,
			    @param_city='Mobile',
			    @param_state='AL',
			    @param_zip='36620',
			    @param_country='USA',
			    @param_lat='30.688990000000004',
			    @param_lon='-88.04466',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Mobile - Government Plaza',
			    @param_email='alicscmobile@gmail.com',
			    @param_phone='251-574-6247',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='8045.0',
			    @param_POSID=@posid;
		 




-- counting: 139 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3301 Vandercar Way',
			    @param_add2=null,
			    @param_city='Cincinnati',
			    @param_state='OH',
			    @param_zip='45209',
			    @param_country='USA',
			    @param_lat='39.15789',
			    @param_lon='-84.4269',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Cincinnati - Oakley ',
			    @param_email='csc-145_oakley@chickensaladchick.com',
			    @param_phone='513-351-1246',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='145.0',
			    @param_POSID=@posid;
		 




-- counting: 140 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='801 Frogmore Dr.',
			    @param_add2=null,
			    @param_city='Baton Rouge',
			    @param_state='LA',
			    @param_zip='70820',
			    @param_country='USA',
			    @param_lat='30.39038',
			    @param_lon='-91.1667',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Baton Rouge, LA',
			    @param_email='csc-107_baton_rouge@chickensaladchick.com',
			    @param_phone='225-478-5050',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='107.0',
			    @param_POSID=@posid;
		 




-- counting: 141 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1121 NW 63rd St',
			    @param_add2=null,
			    @param_city='Nichols Hills',
			    @param_state='OK',
			    @param_zip='73116',
			    @param_country='USA',
			    @param_lat='35.53706',
			    @param_lon='-97.53161',
			    @param_timezoneid='America/New_York',
			    @param_storeName='OK City, OK (Nichols Hills)',
			    @param_email='csc-136_nichols_hills@chickensaladchick.com',
			    @param_phone='(405) 849-6188',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='136.0',
			    @param_POSID=@posid;
		 




-- counting: 142 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='687 Worthington Rd.',
			    @param_add2=null,
			    @param_city='Westerville',
			    @param_state='OH',
			    @param_zip='43082',
			    @param_country='USA',
			    @param_lat='40.14493',
			    @param_lon='-82.95668',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Westerville, OH - Polaris Pkwy',
			    @param_email='csc-132_westerville@chickensaladchick.com',
			    @param_phone='(614) 394-8111',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='132.0',
			    @param_POSID=@posid;
		 




-- counting: 143 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4112 Atlanta Highway',
			    @param_add2=null,
			    @param_city='Loganville',
			    @param_state='GA',
			    @param_zip='30052',
			    @param_country='USA',
			    @param_lat='33.84612',
			    @param_lon='-83.91055',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Loganville, GA - COMING SOON!',
			    @param_email='csc-158_loganville@chickensaladchick.com',
			    @param_phone='334-292-3611',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='158.0',
			    @param_POSID=@posid;
		 




-- counting: 144 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4325 Alexander Dr',
			    @param_add2=null,
			    @param_city='Alpharetta',
			    @param_state='GA',
			    @param_zip='30022',
			    @param_country='USA',
			    @param_lat='34.05936',
			    @param_lon='-84.24606',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Z002 - Prod Test Lab',
			    @param_email='Cameron.Mulvaney@chickensaladchick.com',
			    @param_phone='8777377366',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='998.0',
			    @param_POSID=@posid;
		 




-- counting: 145 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='12536 Olive Blvd',
			    @param_add2=null,
			    @param_city='Creve Coeur',
			    @param_state='MO',
			    @param_zip='63141',
			    @param_country='USA',
			    @param_lat='38.67555',
			    @param_lon='-90.4668',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Creve Coeur, MO',
			    @param_email='csc-120_Creve_coeur@chickensaladchick.com',
			    @param_phone='(314) 548-2141',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='120.0',
			    @param_POSID=@posid;
		 




-- counting: 146 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='6209 Snider Road',
			    @param_add2=null,
			    @param_city='Mason',
			    @param_state='OH',
			    @param_zip='45040',
			    @param_country='USA',
			    @param_lat='39.349109999999996',
			    @param_lon='-84.33085',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Mason, OH',
			    @param_email='csc-150_mason@chickensaladchick.com',
			    @param_phone='513-466-8008',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='150.0',
			    @param_POSID=@posid;
		 




-- counting: 147 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='5135 Goodman Rd STE 100',
			    @param_add2=null,
			    @param_city='Olive Branch',
			    @param_state='MS',
			    @param_zip='38654',
			    @param_country='USA',
			    @param_lat='34.96239',
			    @param_lon='-89.8978',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Olive Branch',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(662) 890-0432',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='73.0',
			    @param_POSID=@posid;
		 




-- counting: 148 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='520 Grapevine Highway',
			    @param_add2=null,
			    @param_city='Hurst',
			    @param_state='TX',
			    @param_zip='76054',
			    @param_country='USA',
			    @param_lat='32.86418',
			    @param_lon='-97.17663',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Hurst',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(817) 857-8503',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='81.0',
			    @param_POSID=@posid;
		 




-- counting: 149 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1817 Cherokee Ave SW ',
			    @param_add2=null,
			    @param_city='Cullman',
			    @param_state='AL',
			    @param_zip='35055',
			    @param_country='USA',
			    @param_lat='34.15448',
			    @param_lon='-86.84085999999999',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Cullman, AL',
			    @param_email='csc-171_cullman@chickensaladchick.com',
			    @param_phone='(256) 787-1760',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='171.0',
			    @param_POSID=@posid;
		 




-- counting: 150 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1118 Ross Clark Cir',
			    @param_add2=null,
			    @param_city='Dothan',
			    @param_state='AL',
			    @param_zip='36301',
			    @param_country='USA',
			    @param_lat='31.216820000000002',
			    @param_lon='-85.36551',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Dothan - Remote',
			    @param_email='csc-9_Dothan@chickensaladchick.com',
			    @param_phone='334-699-3800',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='8009.0',
			    @param_POSID=@posid;
		 




-- counting: 151 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4990 Steiner Way',
			    @param_add2=null,
			    @param_city='Grovetown',
			    @param_state='GA',
			    @param_zip='30813',
			    @param_country='USA',
			    @param_lat='33.48018',
			    @param_lon='-82.2',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Grovetown, GA',
			    @param_email='csc-123_grovetown@chickensaladchick.com',
			    @param_phone='706-432-9622',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='123.0',
			    @param_POSID=@posid;
		 




-- counting: 152 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1760 Dunlawton Ave',
			    @param_add2=null,
			    @param_city='Port Orange',
			    @param_state='FL',
			    @param_zip='32127',
			    @param_country='USA',
			    @param_lat='29.1089',
			    @param_lon='-81.02631',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Port Orange',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='3862655250',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='62.0',
			    @param_POSID=@posid;
		 




-- counting: 153 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='5050 Bayou Boulevard',
			    @param_add2=null,
			    @param_city='Pensacola',
			    @param_state='FL',
			    @param_zip='32503',
			    @param_country='USA',
			    @param_lat='30.473159999999996',
			    @param_lon='-87.2107',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Pensacola, FL',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-275-4578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='113.0',
			    @param_POSID=@posid;
		 




-- counting: 154 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4088 Watson Blvd.',
			    @param_add2=null,
			    @param_city='Warner Robins',
			    @param_state='GA',
			    @param_zip='31093',
			    @param_country='USA',
			    @param_lat='32.615520000000004',
			    @param_lon='-83.70286999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Warner Robins',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='4783333592',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='59.0',
			    @param_POSID=@posid;
		 




-- counting: 155 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='9615 Spring Green Blvd',
			    @param_add2=null,
			    @param_city='Katy',
			    @param_state='TX',
			    @param_zip='77494',
			    @param_country='USA',
			    @param_lat='29.698620000000002',
			    @param_lon='-95.81522',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Katy, TX - Spring Green - COMING SOON!',
			    @param_email='csc-146_katy_cinco@chickensaladchick.com',
			    @param_phone='334-292-3611',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='146.0',
			    @param_POSID=@posid;
		 




-- counting: 156 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='430 Northside Drive East Suite 174',
			    @param_add2=null,
			    @param_city='Statesboro',
			    @param_state='GA',
			    @param_zip='30458',
			    @param_country='USA',
			    @param_lat='32.439370000000004',
			    @param_lon='-81.7627',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Statesboro',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(912) 623-0050',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='87.0',
			    @param_POSID=@posid;
		 




-- counting: 157 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='363 Cox Creek Parkway',
			    @param_add2=null,
			    @param_city='Florence',
			    @param_state='AL',
			    @param_zip='35630',
			    @param_country='USA',
			    @param_lat='34.83965',
			    @param_lon='-87.63644000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Florence, AL',
			    @param_email='csc-144_florence@chickensaladchick.com',
			    @param_phone='256-284-1300',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='144.0',
			    @param_POSID=@posid;
		 




-- counting: 158 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1101 International Pkwy',
			    @param_add2=null,
			    @param_city='Lake Mary',
			    @param_state='FL',
			    @param_zip='32746',
			    @param_country='USA',
			    @param_lat='28.780520000000003',
			    @param_lon='-81.35956999999999',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Lake Mary, FL',
			    @param_email='csc-85_lakemary@chickensaladchick.com',
			    @param_phone='(407) 942-3307',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='85.0',
			    @param_POSID=@posid;
		 




-- counting: 159 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='501 Oxford Exchange Blvd',
			    @param_add2=null,
			    @param_city='Oxford',
			    @param_state='AL',
			    @param_zip='36203',
			    @param_country='USA',
			    @param_lat='33.610929999999996',
			    @param_lon='-85.78504000000001',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Oxford, AL',
			    @param_email='csc-122_oxford@chickensaladchick.com',
			    @param_phone='(256) 403-2412',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='122.0',
			    @param_POSID=@posid;
		 




-- counting: 160 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2050 Gadsden Highway',
			    @param_add2=null,
			    @param_city='Birmingham',
			    @param_state='AL',
			    @param_zip='35235',
			    @param_country='USA',
			    @param_lat='33.612390000000005',
			    @param_lon='-86.62675',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Trussville, AL',
			    @param_email='csc-114_trussville@chickensaladchick.com',
			    @param_phone='205-537-1170',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='114.0',
			    @param_POSID=@posid;
		 




-- counting: 161 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1410 Market St. Ste D3',
			    @param_add2=null,
			    @param_city='Tallahassee',
			    @param_state='FL',
			    @param_zip='32312',
			    @param_country='USA',
			    @param_lat='30.5071',
			    @param_lon='-84.2528',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Tallahassee',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='850-894-2502',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='5.0',
			    @param_POSID=@posid;
		 




-- counting: 162 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3219-B North Oak Street Extension',
			    @param_add2=null,
			    @param_city='Valdosta',
			    @param_state='GA',
			    @param_zip='31603',
			    @param_country='USA',
			    @param_lat='30.8842',
			    @param_lon='-83.2911',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Valdosta',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='229-469-7017',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='6.0',
			    @param_POSID=@posid;
		 




-- counting: 163 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2511 Airport Thruway, ste. C',
			    @param_add2=null,
			    @param_city='Columbus',
			    @param_state='GA',
			    @param_zip='31904',
			    @param_country='USA',
			    @param_lat='32.5207',
			    @param_lon='-84.9576',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Columbus',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='706-507-1611',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='3.0',
			    @param_POSID=@posid;
		 




-- counting: 164 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3850 West Main Street Unit 402',
			    @param_add2=null,
			    @param_city='Dothan',
			    @param_state='AL',
			    @param_zip='36305',
			    @param_country='USA',
			    @param_lat='31.2345',
			    @param_lon='-85.4506',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Dothan',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='334-699-3800',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='9.0',
			    @param_POSID=@posid;
		 




-- counting: 165 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2222 Augusta Street, Unit 6',
			    @param_add2=null,
			    @param_city='Greenville',
			    @param_state='SC',
			    @param_zip='29605',
			    @param_country='USA',
			    @param_lat='34.8227',
			    @param_lon='-82.3926',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Greenville',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='864-451-7790',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='8.0',
			    @param_POSID=@posid;
		 




-- counting: 166 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1345 Opelika Rd',
			    @param_add2=null,
			    @param_city='Auburn',
			    @param_state='AL',
			    @param_zip='36830',
			    @param_country='USA',
			    @param_lat='32.62173',
			    @param_lon='-85.4537',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Auburn',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='3348217770',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='1.0',
			    @param_POSID=@posid;
		 




-- counting: 167 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='1800 McFarland Blvd, Unit 308',
			    @param_add2=null,
			    @param_city='Tuscaloosa',
			    @param_state='AL',
			    @param_zip='35404',
			    @param_country='USA',
			    @param_lat='33.1965',
			    @param_lon='-87.5271',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Tuscaloosa',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='205-462-3594',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='13.0',
			    @param_POSID=@posid;
		 




-- counting: 168 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '783BDFBA-694B-4976-AC86-A1FB5BE59693');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='724 North Dean Rd',
			    @param_add2=null,
			    @param_city='Auburn',
			    @param_state='AL',
			    @param_zip='36830',
			    @param_country='USA',
			    @param_lat='32.6211',
			    @param_lon='-85.4616',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Chicken Salad Corperate HQ',
			    @param_email='info@chickensaladchick.com',
			    @param_phone='334-275-4578',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='24.0',
			    @param_POSID=@posid;
		 




-- counting: 169 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3780 Riverchase Village Suite 110',
			    @param_add2=null,
			    @param_city='Hoover',
			    @param_state='AL',
			    @param_zip='35244',
			    @param_country='USA',
			    @param_lat='33.37762',
			    @param_lon='-86.80054',
			    @param_timezoneid='America/Chicago',
			    @param_storeName='Birmingham - Riverchase',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='(205) 518-0256',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='54.0',
			    @param_POSID=@posid;
		 




-- counting: 170 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='3026 College Park Drive',
			    @param_add2=null,
			    @param_city='Conroe',
			    @param_state='TX',
			    @param_zip='77884',
			    @param_country='USA',
			    @param_lat='30.20822',
			    @param_lon='-95.46166',
			    @param_timezoneid='America/New_York',
			    @param_storeName='College Park, TX',
			    @param_email='csc-128_conroe@chickensaladchick.com',
			    @param_phone='(936) 224-7959',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='128.0',
			    @param_POSID=@posid;
		 




-- counting: 171 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='410 Peachtree Pkwy',
			    @param_add2=null,
			    @param_city='Cumming',
			    @param_state='GA',
			    @param_zip='30041',
			    @param_country='USA',
			    @param_lat='34.15417',
			    @param_lon='-84.17915',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Cumming, GA',
			    @param_email='csc-90_cumming@chickensaladchick.com',
			    @param_phone='(470) 533-2703',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='90.0',
			    @param_POSID=@posid;
		 




-- counting: 172 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='4429 Washington Rd',
			    @param_add2=null,
			    @param_city='Evans',
			    @param_state='GA',
			    @param_zip='30809',
			    @param_country='USA',
			    @param_lat='33.54377',
			    @param_lon='-82.13909',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Evans, GA',
			    @param_email='CSC-83_Evans@chickensaladchick.com',
			    @param_phone='(762) 224-2280',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='83.0',
			    @param_POSID=@posid;
		 




-- counting: 173 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='21930 Kuykendahl Rd',
			    @param_add2=null,
			    @param_city='Spring',
			    @param_state='TX',
			    @param_zip='77388',
			    @param_country='USA',
			    @param_lat='30.08432',
			    @param_lon='-95.52628',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Spring, TX ',
			    @param_email='csc-109_spring@chickensaladchick.com',
			    @param_phone='(832) 698-2056',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='109.0',
			    @param_POSID=@posid;
		 




-- counting: 174 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='264 SE John Jones Drive',
			    @param_add2=null,
			    @param_city='Burleson',
			    @param_state='TX',
			    @param_zip='76028',
			    @param_country='USA',
			    @param_lat='32.51938',
			    @param_lon='-97.34949',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Burleson, TX',
			    @param_email='csc-127_burleson@chickensaladchick.com',
			    @param_phone='(817) 857-8505',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='127.0',
			    @param_POSID=@posid;
		 




-- counting: 175 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='8008 Kingston Pike',
			    @param_add2=null,
			    @param_city='Knoxville',
			    @param_state='TN',
			    @param_zip='37923',
			    @param_country='USA',
			    @param_lat='35.93398',
			    @param_lon='-84.04958',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Knoxville, TN',
			    @param_email='marketing@chickensaladchick.com',
			    @param_phone='865-357-1587',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='93.0',
			    @param_POSID=@posid;
		 




-- counting: 176 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='2776 Enterprise Drive',
			    @param_add2=null,
			    @param_city='Opelika',
			    @param_state='AL',
			    @param_zip='36801',
			    @param_country='USA',
			    @param_lat='32.61615',
			    @param_lon='-85.40785',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Opelika, AL (Tiger Town)',
			    @param_email='csc-117_opelika@chickensaladchick.com',
			    @param_phone='334-203-1449',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='117.0',
			    @param_POSID=@posid;
		 




-- counting: 177 
 
			declare @retailerid uniqueidentifier;
			declare @storeid uniqueidentifier;
			declare @addressid uniqueidentifier;
			declare @posid uniqueidentifier;

			set @retailerid=convert(uniqueidentifier, 'F1DD4BB4-B5F4-45CC-997D-4543E0C2BB96');
			set @posid=convert(uniqueidentifier, '37716B5A-BDAE-4F1E-AE1F-48D9A9765277');
			set @storeid=newid();
			set @addressid=newid();

			exec Broker._Setup_RegisterStore 
			    @param_scanexpiration=10080,
			    @param_RetailerID=@retailerid,
			    @param_StoreID=@storeid,
			    @param_addressID=@addressid,
			    @param_add1='9516 Riverbend Village Drive',
			    @param_add2=null,
			    @param_city='Charlotte',
			    @param_state='NC',
			    @param_zip='28216',
			    @param_country='USA',
			    @param_lat='35.32707',
			    @param_lon='-80.94206',
			    @param_timezoneid='America/New_York',
			    @param_storeName='Charlotte - Riverbend',
			    @param_email='CSC-147_Riverbend@chickensaladchick.com',
			    @param_phone='(980) 218-9537',
			    @param_openFrom=null,
			    @param_openTo=null,
			    @param_daysOfWeek=7,
			    @param_posstorekey='147.0',
			    @param_POSID=@posid;
		 




