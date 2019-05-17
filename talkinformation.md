Steps to add/update information about a talk:
1. Creation of file. Duplicate the file "template_talk.html" with the name "YYYYMMDD.html" where YYYYMMDD is the date of the talk in the folder "Talks". This will make the identifier unique and systematic. If the talk is at Urania, one can use "template_BMSFriday_talk_at_Urania.html".

2. Meta information. Put the title of the talk in the meta tag title and below the complete name of the speaker in the meta tag of the description. The name of the talk should be included here as "What is/are TOPIC-OF-THE-TALK?". Note: Cancel the "are" comment if not used (else it appears at the top of the page.

3. Update information of the talk in the body.
-Choose "What is..." or "What are..." depending on grammatical number of what comes next. Just erase the one that does not belong there.
-Title
	+Title should go in the place of "whatever the talk is about" (without the particle "What is/are" of the beginning which is already included in a fancy form).
	+One should avoid capitalization in the title. If this is an old talk, one should make sure that the title in the talks lists in "talks.html" is not capitalized at all.
-Speaker
	+Complete name of the speaker where "Speaker" is.
	+Institution of the speaker where "University Berlin" is. Use "FU/HU/TU Berlin" instead of just "FU/HU/TU".
-Date
	+Date of the talk of the talk in the place of "YYYY/MM/DD"
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
	+Abstract of the talk where the sequence of consecutive "bla " is.
	+For a paragraph break, use "</p><p>" adding the substituting the "<p>" of the old paragraph environment by "<p style="margin:0;">" so that there is no space between the paragraphs. Also one can just employ "<br>", but this is not a good practice in HTML programming.
-Video
	+Check if there is a public video of the talk in Vimeo
	+If that's the case, uncomment the Vimeo video code pasting the numerical code of the Video in the place of the number 160594229 that is in the address between "video/" and "?color=".

4. Update the "talks.html" file. Add the infomation of the talk to the talks list.
-Date. Add the date in the format YYYY/MM/DD
-Venue. Add the correponding two letters code (FU, HU, TU, Ur, for Urania; or Ot, for other).
-Title should be without any suspensive dots and without any fancy form of the beginning of the question. The italics are automatic. Again, make sure the title is not capitalized.
-Speaker. Put the complete name of the speaker with the institution between parentheses. In the case of any of the three Berlin universities, use the short form FU, HU or TU.
-Link. Check that the link points to the correct file and it is of the form:
	<a href="talks/YYYYMMDD.html" class="fas fa-link"></a>

5.Update the sitemap.xml file by adding the code
<url>
<loc>https://whatisseminar.xyz/talks/YYYYMMDD.html</loc>
<lastmod>YYYY-MM-DD</lastmod>
</url>
where the first date is the identifier of the HTML file of the talk and the second one the day of creation modification of the talk. If the file is just being modified, then just update the date of the code present in the XML file.

6. If this is a current talk, paste the relevant part of the code in the currenttalk.html file, so that it remains updated. Don't erase the sentences concerning the weeks that there are no talks. These has just to be commented out.
