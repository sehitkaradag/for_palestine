import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_icon = "Flag_of_Palestine_Flat_Round.png" ,page_title = "Palestine starterkit")

st.title("Palestina protesten en informatie")

data_df = pd.DataFrame(
    {   
        "Datum": [datetime(2023,11,12,19,0), datetime(2023,11,16,19,30), datetime(2023,11,18,13,0), datetime(2023,11,18,13,0), datetime(2023,11,19,14,0)],
        "Locatie": ["Amsterdam, centraal station", "Leeuwarden, stationsplein", "Amsterdam, Dam", "Leeuwarden, stationsplein", "Rotterdam, binnenrotte"]
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

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Zelf actie voeren","Boycott","Petities","Schrijf politici","Spullen","Posters"])

with tab1:
    st.subheader("Zelf actie voeren", divider='red')
    st.write("Hoe meer demonstraties & acties, hoe beter! Het is super belangrijk dat we op zoveel mogelijk plekken van ons laten horen. Een actie of demonstratie kan zo groot of klein zijn als je zelf wilt - je kunt zonder voorbereiding in je eentje op een drukke plek gaan staan met een pakkend bord of leuzen op de stoep krijten. Maar je kan ook een demonstratie met duizenden mensen organiseren, en van alles daar tussenin.")
    st.link_button(":red[Demonstratie starterkit]","https://drive.google.com/file/d/10XuVK22QailEljV--nZ7Ca-1Xc1tXvSx/view?usp=sharing")
with tab2:
    st.subheader("Boycott", divider='red')
    st.write("Koop geen spullen uit Israël, of van bedrijven die de Israëlische bezetting steunen. Een paar tips:")
    
    tab2_col1, tab2_col2 = st.columns(2)
    tab2_col1.write("Check in de supermarkt waar producten vandaan komen! Koop geen spullen uit Israël. Eventueel kun je stickers op de producten plakken om ook andere mensen te waarschuwen.")
    tab2_col1.link_button(":red[Bestel je stickers hier]","https://shop.palestinecampaign.org/products/500-boycott-israeli-apartheid-stickers")

    tab_col2.write("Boycot merken die het Israelische regime actief steunen. De organisatie BDS adviseert om met zo veel mogelijk mensen een klein aantal bedrijven te boycotten. Je kan deze bedrijven natuurlijk ook een bericht sturen of een actie organiseren om extra druk uit te oefenen.")
    tab2_col2.link_button(":red[Volg BDS (Boycot, Divest, Sanction)]", "https://bdsmovement.net/get-involved/join-a-bds-campaign")
    tab2_col2.link_button(":red[Palestina Komitee]", "https://palestina-komitee.nl/")
    tab2_col2.link_button(":red[BDS Nederland]","https://bdsnederland.nl/")
    tab2_col2.link_button(":red[Waarom is een Boycott nodig?]", "http://www.inminds.com/boycott-israel-2012.php")


with tab3:
    st.write("text")

with tab4:
    st.write("text")

with tab5:
    st.write("text")

with tab6:
    st.write("text")
