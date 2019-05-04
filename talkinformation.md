Steps to add/update information about a talk:
1. Creation of file. Duplicate the file "template_talk.html" with the name "YYYYMMDD.html" where YYYYMMDD is the date of the talk in the folder "Talks". This will make the identifier unique and systematic.
2. Meta information. Put the title of the talk in the meta tag title and below the complete name of the speaker in the meta tag of the description. The name of the talk should be included here as "What is/are TOPIC-OF-THE-TALK?"
3. Update information of the talk in the body.
-Title
	+Title should go in the place of "whatever the talk is about" (without the particle "What is/are" of the beginning which is included in a fancy form already).
-Speaker
	+Complete name of the speaker where "Speaker" is.
	+Institution of the speaker where "Institution" is. Use "FU/HU/TU Berlin" instead of just "FU/HU/TU".
-Date
	+Date of the talk of the talk in the place of "YYY/MM/DD"
	+Time of the talk in the place of "13:00".
	+If the talk takes place on a BMS Friday uncomment the break and put the complete name of the professor in the place of "XYZ".
	+If the talk took place during the BMS Days add to this line "during the BMS Days". Similarly for other special BMS events.
-Location
	+Location of the talk where "Place" is. 
	+The most common one will be "Urania Berlin, at BMS Loft (3rd floor)", but one should check that the talk didn't took place at another floor.
	+For FU, HU and TU, the format will be "FU/HU/TU Berlin, at room IDENTIFICATION-NUMBER (Street-name and number of building)", except for two exceptions which are:
		* "HU Berlin, at BMS Seminar Room (RUD 25 1.023)"
		* "TU Berlin, at BMS Seminar Room (MA212)"
-Abstract
	+Abstract of the talk where the sequence of consequtive "bla " is.
	+For a paragraph break, use "</p><p>" adding the substituting the "<p>" of the old paragraph environment by "<p style="margin:0;">" so that there is no space between the paragraphs.
-Video
	+Check if there is a public video of the talk in Vimeo
	+If that's the case, uncomment the Vimeo video code pasting the numerical code of the Video in the place of the number 160594229 that is in the address between "video/" and "?color=".
4.Update the sitemap.xml file by adding the code
<url>
<loc>https://whatisseminar.xyz/talks/YYYMMDD.html</loc>
<lastmod>YYYY-MM-DD</lastmod>
</url>
where the first date is the identifier of the HTML file of the talk and the second one the day of creation modification of the talk. If the file is just being modified, then just update the date of the code present in the XML file.
5. If this is a current talk, paste the relevant part of the code in the currenttalk.html file, so that it remains updated.
