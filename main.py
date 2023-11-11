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
    data_df,
    column_config={
        "Datum": st.column_config.DatetimeColumn(
            "Datum",
            min_value = datetime(2023,11,11),
            max_value = dateime(2024,12,30),
            format = "D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)
st.dataframe(data_df)


st.subheader("Zelf actie voeren", divider='red')

st.write("Hoe meer demonstraties & acties, hoe beter! Het is super belangrijk dat we op zoveel mogelijk plekken van ons laten horen. Een actie of demonstratie kan zo groot of klein zijn als je zelf wilt - je kunt zonder voorbereiding in je eentje op een drukke plek gaan staan met een pakkend bord of leuzen op de stoep krijten. Maar je kan ook een demonstratie met duizenden mensen organiseren, en van alles daar tussenin.")
st.link_button(":red[Demonstratie starterkit]","https://drive.google.com/file/d/10XuVK22QailEljV--nZ7Ca-1Xc1tXvSx/view?usp=sharing")

st.subheader("Boycott", divider='red')

st.write("Hoe meer demonstraties & acties, hoe beter! Het is super belangrijk dat we op zoveel mogelijk plekken van ons laten horen. Een actie of demonstratie kan zo groot of klein zijn als je zelf wilt - je kunt zonder voorbereiding in je eentje op een drukke plek gaan staan met een pakkend bord of leuzen op de stoep krijten. Maar je kan ook een demonstratie met duizenden mensen organiseren, en van alles daar tussenin.")
st.link_button(":red[Demonstratie starterkit]","https://drive.google.com/file/d/10XuVK22QailEljV--nZ7Ca-1Xc1tXvSx/view?usp=sharing")
