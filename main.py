import streamlit as st
import pandas as pd

st.set_page_config(page_icon = "Flag_of_Palestine_Flat_Round.png" ,page_title = "Palestine starterkit")

st.title("Palestina protesten en informatie")

data_df = pd.DataFrame(
    {   
        "Datum": [datetime(2024,11,12,19,0), datetime(2024,11,16,19,30), datetime(2024,11,18,13,0), datetime(2024,11,18,13,0), datetime(2024,11,19,14,0)],
        "Locatie": ["Amsterdam, centraal station", "Leeuwarden, stationsplein", "Amsterdam, Dam", "Leeuwarden, stationsplein", "Rotterdam, binnenrotte"]
    }
)



st.subheader("Zelf actie voeren", divider='red')

st.write("Hoe meer demonstraties & acties, hoe beter! Het is super belangrijk dat we op zoveel mogelijk plekken van ons laten horen. Een actie of demonstratie kan zo groot of klein zijn als je zelf wilt - je kunt zonder voorbereiding in je eentje op een drukke plek gaan staan met een pakkend bord of leuzen op de stoep krijten. Maar je kan ook een demonstratie met duizenden mensen organiseren, en van alles daar tussenin.")
st.link_button(":red[Demonstratie starterkit]","https://drive.google.com/file/d/10XuVK22QailEljV--nZ7Ca-1Xc1tXvSx/view?usp=sharing")

st.subheader("Boycott", divider='red')

st.write("Hoe meer demonstraties & acties, hoe beter! Het is super belangrijk dat we op zoveel mogelijk plekken van ons laten horen. Een actie of demonstratie kan zo groot of klein zijn als je zelf wilt - je kunt zonder voorbereiding in je eentje op een drukke plek gaan staan met een pakkend bord of leuzen op de stoep krijten. Maar je kan ook een demonstratie met duizenden mensen organiseren, en van alles daar tussenin.")
st.link_button(":red[Demonstratie starterkit]","https://drive.google.com/file/d/10XuVK22QailEljV--nZ7Ca-1Xc1tXvSx/view?usp=sharing")
