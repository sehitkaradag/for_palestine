import streamlit as st
import pandas as pd
from datetime import datetime

######################################
# Page configuration & Sidebar
######################################

st.set_page_config(page_icon = "Flag_of_Palestine_Flat_Round.png" ,page_title = "Palestine starterkit")

with st.sidebar:
    st.link_button(":red[Nieuwe demonstratie melden]", "https://forms.gle/QgroohXDBk1ntpjB8")
    st.link_button(":green[Feedback of vragen]","https://forms.gle/UPAEQsUGxJ4SdTK57")

######################################
# Page title & Dataframe display
######################################
st.title("Palestina protesten en informatie")

data_df = pd.DataFrame(
    {   
        "Datum": [datetime(2023,11,14,18,0),
        datetime(2023,11,14,19,0),
        datetime(2023,11,15,19,0), 
        datetime(2023,11,16,19,30),
        datetime(2023,11,17,19,0), 
        datetime(2023,11,18,13,0), 
        datetime(2023,11,18,13,0),
        datetime(2023,11,18,19,0), 
        datetime(2023,11,19,14,0)
        datetime(2023,11,19,19,0)]
        "Locatie": ["Amsterdam, Schiphol Plaza",
         "Amsterdam, Centraal Station",
         "Amsterdam, Centraal Station",
         "Leeuwarden, Stationsplein",
         "Amsterdam, Centraal Station",
         "Amsterdam, Dam", 
         "Leeuwarden, Stationsplein",
         "Amsterdam, Centraal Station",
         "Rotterdam, Binnenrotte",
         "Amsterdam, Centraal Station"]
    }
)
st.data_editor(
    data_df,use_container_width=True,
    column_config={
        "Datum": st.column_config.DatetimeColumn(
            "Datum",
            min_value = datetime(2023,11,11),
            max_value = datetime(2024,12,30),
            format = "D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)
st.caption("Nieuwe demonstraties worden dagelijks toegevoegd")

######################################
# Display of tabs. 6 tabs in total with some containing columns
######################################


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Zelf actie voeren","Boycott","Petities","Schrijf politici","Spullen","Posters"])

with tab1:
    st.subheader("Zelf actie voeren", divider='red')
    st.write("Hoe meer demonstraties & acties, hoe beter! Het is super belangrijk dat we op zoveel mogelijk plekken van ons laten horen. Een actie of demonstratie kan zo groot of klein zijn als je zelf wilt - je kunt zonder voorbereiding in je eentje op een drukke plek gaan staan met een pakkend bord of leuzen op de stoep krijten. Maar je kan ook een demonstratie met duizenden mensen organiseren, en van alles daar tussenin.")
    st.link_button(":red[Demonstratie starterkit]","https://drive.google.com/file/d/10XuVK22QailEljV--nZ7Ca-1Xc1tXvSx/view?usp=sharing")
    st.link_button(":red[Banners (they have names)]","https://theyhavenames.net/how-to-find/")
with tab2:
    st.subheader("Boycott", divider='red')
    st.write("Koop geen spullen uit Israël, of van bedrijven die de Israëlische bezetting steunen. Een paar tips:")
    
    tab2_col1, tab2_col2 = st.columns(2)
    tab2_col1.write("Check in de supermarkt waar producten vandaan komen! Koop geen spullen uit Israël. Eventueel kun je stickers op de producten plakken om ook andere mensen te waarschuwen.")
    tab2_col1.link_button(":red[Bestel je stickers hier]","https://shop.palestinecampaign.org/products/500-boycott-israeli-apartheid-stickers")

    tab2_col2.write("Boycot merken die het Israelische regime actief steunen. De organisatie BDS adviseert om met zo veel mogelijk mensen een klein aantal bedrijven te boycotten. Je kan deze bedrijven natuurlijk ook een bericht sturen of een actie organiseren om extra druk uit te oefenen.")
    tab2_col2.link_button(":red[Volg BDS (Boycot, Divest, Sanction)]", "https://bdsmovement.net/get-involved/join-a-bds-campaign")
    tab2_col2.link_button(":red[Palestina Komitee]", "https://palestina-komitee.nl/")
    tab2_col2.link_button(":red[BDS Nederland]","https://bdsnederland.nl/")
    tab2_col2.link_button(":red[Waarom is een Boycott nodig?]", "http://www.inminds.com/boycott-israel-2012.php")


with tab3:
    st.subheader("Petities", divider='red')
    st.write("Het is belangrijk om ook schriftelijk je stem te laten horen. Teken daarom de volgende petities:")
    tab3_col1, tab3_col2 = st.columns(2)

    tab3_col1.link_button(":green[Zorgmedewerkers]","https://docs.google.com/forms/d/e/1FAIpQLSeHKSl6nKWhZjyBQBSBY0fHyd1JJ6HO5GPk-b4HteZmfTlbuA/viewform")
    tab3_col1.link_button(":green[Nederlanders]","https://artikel90nu.petities.nl/")
    tab3_col1.link_button(":green[Voor ambtenaren]","https://docs.google.com/forms/d/e/1FAIpQLScdDs12Fo6C2SyzoPkWDQk-IlZEo6_NQb8_WEkGxkWqQBzK3A/viewform")
    tab3_col1.link_button(":green[Academici en studenten in NL]","https://docs.google.com/forms/d/e/1FAIpQLSc5iBdA7MXwj8Fv5YVSCSTO-9aMxgq2CVHINnDJYfkh7TeNoA/viewform")


    tab3_col2.link_button(":red[Ceasefire Now]","https://www.change.org/p/sign-and-share-this-urgent-petition-calling-for-a-ceasefirenow-in-gaza-and-israel?utm_content=cl_sharecopy_37700646_en-GB%3A4&recruited_by_id=3af7eb40-728f-11ee-9fc7-bdef27e43073&utm_source=share_petition&utm_medium=copylink&utm_campaign=psf_combo_share_initial")
    tab3_col2.link_button(":red[Stop the bloodshed of Children in Gaza]","https://secure.avaaz.org/campaign/nl/israel_palestine_save_the_kids_loc/")
    tab3_col2.link_button(":red[Ceasefire, Stop the war]","https://secure.avaaz.org/campaign/en/call_for_sanity_3_1/")
    tab3_col2.link_button(":red[Stop the genocide and recognize the human rights of the Palestinians]", "https://petities.nl/petitions/stop-de-genocide-en-erken-de-mensenrechten-van-de-palestijnen?locale=nl")
    tab3_col2.link_button(":red[Take a stand against the violatuons of human rights in Gaza]","https://petities.nl/petitions/neem-stelling-tegen-de-schending-van-de-mensenrechten-in-gaza/signatures/28425707?locale=nl")
    tab3_col2.link_button(":red[The Rights Forum: The Hague is working on peace]","https://rightsforum.org/petitie/den-haag-maak-nu-werk-vrede-israel-palestina/")
    tab3_col2.link_button(":red[Pax - Don't give Israel a carte blanche]","https://paxvoorvrede.nl/acties/geen-carte-blanche/")
    

with tab4:
    st.subheader("Schrijf politici", divider='red')
    st.write("Schrijf aan politici en eis verandering van Nederland in onze houding ten opzichte van Israël en Palestina. Plant een Olijfboom heeft een voorbeeldbrief en de e-mail adressen van Tweede Kamerleden:")
    st.link_button(":red[Brief template]","https://www.planteenolijfboom.nl/brief-politiek")
    st.link_button(":green[Tweedekamerleden email template]", "https://tinyurl.com/yp9hf3k6")

with tab5:
    st.subheader("Spullen", divider='red')
    st.write("Met spullen kun je natuurlijk ook uitdragen dat je Palestina steunt.")
    st.link_button(":red[handmadepalestine.com]","https://handmadepalestine.com/")
    st.link_button(":red[fairtradepalestine.org]","https://www.fairtradepalestine.org/")
    st.link_button(":red[madeinpalestine.de]", "https://www.madeinpalestine.de/")
    st.link_button(":green[Shirt]", "https://derodelap.nl/product/free-palestine-shirt-pre-order/")
    st.link_button(":green[Button]", "https://derodelap.nl/product/palestijnse-vlag-pin/")
    st.link_button(":green[Kufiya]","https://www.kufiya.org/")
    st.link_button(":green[Stickers]", "https://leftlaser.com/collections/propaganda-1/products/free-palestine-sticker")
    st.link_button(":green[Autostickers]","https://www.vlaggenclub.nl/auto-sticker-palestijnse-vlag")

with tab6:
    st.subheader("Posters", divider='red')
    st.write("Koop of print posters. Print ze uit en plak ze op je raam of neem ze mee naar een demonstratie! Je kan natuurlijk ook tientallen of honderden posters printen en deze op zogenaamde plakzuilen plakken. Bijvoorbeeld op plakzuilen, waar iedereen wild mag plakken.")
    st.link_button(":red[Palestina posters]","https://drive.google.com/drive/folders/1Qsv4WQiUbNnCZuEP6wwUIrOsLm1NqW5W")
    st.link_button(":red[Tips over posters plakken]", "https://www.greenpeace.org/nl/stoomcursus-stickers-posters-plakken/")

######################################
# CSS banner down the page for donations
######################################
st.markdown(
    """
<style>
body {
	margin-top: 35px;
}
.support-palestine, .support-palestine:visited {
	position: absolute;
	left: 0;
	top: 0;
	right: 0;
	background: rgb(0,0,0);
	display: flex;
	justify-content: center;
	padding-top: 5px;
	padding-bottom: 5px;
	z-index: 10000;
	text-decoration: none;
	font-family: arial;
}
.support-palestine:hover, .support-palestine:active {
	background: black;
	display: flex;
	background: rgb(25, 25, 25);
	text-decoration: none;
}
.support-palestine__flag {

	margin-right: 10px;
}

.support-palestine__label {
	color: white;
	font-size: 12px;
	line-height: 24px;
}
.background {
  background: darkgreen;

height:21px;
} 
.top { 
  background: black;
  width:40px;
  height: 8px;
  z-index: 1;
}
.middle {
  background: white;
  width: 100%;
  height: 8px;
  z-index: 1;
}
.triangle {
  background: auto;
  border-top: 12px solid transparent;
  border-bottom: 12px solid transparent;
  border-left: 20px solid red;
  z-index: 2;
  position: relative;
  top: -16px;
  left: 0;
}
</style>
<a class="support-palestine" href="https://www.islamic-relief.org.uk/giving/appeals/palestine/" target="_blank" rel="nofollow noopener" title="Donate to support palestine">
	<div class="support-palestine__flag" role="img" aria-label="Flag of palestine">
	<div class="background">
  <div class="top"></div>
  <div class="middle"></div>
  <div class="triangle"></div>
</div>
	</div>
	<div class="support-palestine__label">
		Donate to support Palestine
	</div>
</a>
""",
    unsafe_allow_html=True,
)

st.markdown("""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11409332455">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-11409332455');
</script>  
""", 
    unsafe_allow_html=True,
)
