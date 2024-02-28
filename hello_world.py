import streamlit as st
import pandas as pd
import numpy as np

# Obligatorische Abschnitte
# Text-Elemente
st.title("Hello World App")
st.header("Willkommen in der modernen und stylischen Welt") 
st.subheader('DIESE APP ist :sparkles: magisch :sunglasses:')
st.write("🌸 Herzlich Willkommen in der modernen und stylischen Welt der Hello World App! 🌸")

# Daten-Elemente
st.header("Tabelle mit Stars")
st.subheader("Diese weiblichen und männlichen Stars sind auch in der Fashion Welt bekannt:")
celebrity_data = {'Name': ['Ariana Grande', 'Jennifer Lawrence', 'Zendaya', 'Scarlett Johansson', 'Angelina Jolie',
                           'Jason Statham', 'Vin Diesel', 'Tom Holland', 'Michael B Jordan', 'Chris Hemsworth'],
                  'Geschlecht': ['Weiblich', 'Weiblich', 'Weiblich', 'Weiblich', 'Weiblich',
                                 'Männlich', 'Männlich', 'Männlich', 'Männlich', 'Männlich'],
                  'Alter': [21, 30, 25, 35, 32, 54, 54, 25, 34, 38],
                  'Beruf': ['Sängerin', 'Sängerin', 'Schauspielerin', 'Schauspielerin', 'Schauspielerin',
                            'Schauspieler', 'Schauspieler', 'Schauspieler', 'Schauspieler', 'Schauspieler'],
                  'Hobby': ['Musik', 'Songwriting', 'Mode', 'Humanitäre Arbeit', 'Reisen',
                            'Auto-Fans', 'Action-Filme', 'Spider-Man spielen', 'Fitness', 'Thor spielen']}
celebrity_df = pd.DataFrame(celebrity_data)

# Styling für die Tabelle hinzufügen
def highlight_gender(val):
    if val == 'Weiblich':
        return 'background-color: #ffc0cb; color: #000; text-align: center;'  # Pink für "Weiblich"
    elif val == 'Männlich':
        return 'background-color: #add8e6; color: #000; text-align: center;'  # Blau für "Männlich"
    else:
        return 'text-align: center;'

st.dataframe(celebrity_df.style.applymap(highlight_gender))

# Chart-Elemente
st.header("Stylische Chart-Elemente")
st.subheader("Fashion-Trenddiagramm:")
trend_data = pd.DataFrame(np.random.randn(20, 3), columns=['Fashion', 'Style', 'Glamour'])
st.line_chart(trend_data)

# Eingabe-Widgets
st.header("Eingabe-Widgets für den stylischen Look")
st.subheader("Stylischer Schieberegler:")
style_value = st.slider("Wähle einen Style-Wert", 0, 100, 50)

# Sidebar als Beispiel für Layout und Container
st.sidebar.header("Sidebar für stylisches Layout")
with st.sidebar:
    st.sidebar.subheader("Über Fashion:")
    st.sidebar.write("Entdecke die neuesten Trends und Styles.")
    st.sidebar.subheader("Tipps:")
    st.sidebar.write("Klicke auf 'Fashion Show starten!' für eine magische Erfahrung.")
    if st.sidebar.button("Fashion Show starten!"):
        st.success("Die Fashion Show beginnt jetzt! 🎉👠💄")

# Kreativer Abschnitt
st.header("Fashionista 🎨")
st.subheader("Gestalte deine stylische Welt!")
fashion_color = st.color_picker("Wähle eine stylische Farbe", "#ff80ab")
st.markdown(f"Gewählte stylische Farbe: **{fashion_color}**")

# Weitere kreative Elemente
st.header("Weitere Kreative Elemente")

# Stylische Symbole
st.subheader("Stylische Symbole:")
st.write("💅👜👗👠🌸")

# Inspirierende Musik
st.subheader("Inspirierende Playlist:")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3")

# Schicke Zitate
st.subheader("Fashion-Zitate:")
fashion_quote = st.selectbox("Wähle ein Fashion-Zitat", ["Eleganz ist die einzige Schönheit, die niemals verblasst.",
                                                          "Kleide dich, als würdest du bereits die Rolle leben, die du spielen willst.",
                                                          "Schönheit beginnt in dem Moment, in dem du beschließt, du selbst zu sein."])
st.write(f"_{fashion_quote}_")

# Konfetti anstelle von Luftballons
st.header("Nur mit einem Klick")
if st.button("Klick für eine Überraschung!"):
    st.balloons()  # Konfetti

# Erstelle einen DataFrame mit Latitude- und Longitude-Spalten
location_data = {'LAT': [37.7749], 'LON': [-122.4194]}
location_df = pd.DataFrame(location_data)

# Schicke Karte
st.header("Stylische Karte 🗺️")
st.map(location_df, use_container_width=True)

# Zeige die App an
st.button("Klick für einen stylischen Start")
