import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
import time 
import os
import pathlib
import streamlit.components.v1 as components


st.title("Welcome to (a sneak peek of) footyLab!")
iframe_src3 = "https://www.youtube.com/embed/wBY0Qlk_djU?si=7yaVJXCdvYXkXxcq"
components.iframe(iframe_src3,600,400)
#if st.button("Best ever"):
#      st.image("https://www.si.com/.image/t_share/MTc5NTMwMzAxNjQ1NTMwMjQ5/gettyimages-891445.jpg")

st.header("Here, Coach Gus (yours truly), will provide information and examples to help you on your path to building your own app.")

#st.text("This is the home page of our currently-under-development app!")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.text("The goal is for us to explore the data we have been collecting on the soccer field right here in the footyLab.")
        st.subheader("BUT HOW ARE WE GONNA DO THIS?!")
        st.markdown("Magic. Well... actually by writing some *python code*... which feels like magic, I promise.")

        st.header("Hacking Skills = ~Computer Programming~ *Magic*")
        iframe_src2 = "https://www.youtube.com/embed/Qgr4dcsY-60?si=gsK8I_rpz0cpH5UO"
        components.iframe(iframe_src2,400,300)
        st.caption("This clip is a great example of what we mean by using proper _syntax_. Hermione used the correct syntax, :green[so the spell worked]! Seamus used incorrect syntax :red[so the spell didn't work] and now he needs a new feather. It is very normal to make mistakes when coding. :blue[If something isn't working, check to make sure you used the proper syntax.]")

coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Now I'm going to ``cast a spell`` (:wink:) to generate a button:")

        st.code("""
               #this spell is actually just python code
        st.button("I'm a Button")
                """)
        st.button("I'm a Button")

coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Okay cool! We can click on our newly casted button but... that's about it. Let's try a slightly more advanced spell:")

        st.code("""
        if st.button("Click me for a celebration"):
                st.balloons()
                """)

        if st.button("Click me for a celebration"):
                st.balloons()

st.subheader("See? Magic.")
#st.page_link("https://docs.streamlit.io/develop/api-reference", label="Click me to read about more Streamlit ~~methods~~ spells", icon="🪄")
st.divider()

st.title("Your Brain, Electricity, Some Stuff Called 'Myelin', and Getting Better at Stuff.")
col1, col2 = st.columns(2)
with col2:
        st.image(image="./media/myelin_sheath.jpg",width=400)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/resistance-in-a-wire/latest/resistance-in-a-wire_en.html"
        components.iframe(iframe_src,height=500)


st.divider()

st.write("Using our magic analogy, we borrow some *spells* from our *spellbooks*:")
st.code(""" 
        import streamlit as st
        import pandas as pd
        """)
st.write('streamlit and pandas are just some of the spellbooks we will use. This is just python code other people have written and kindly made available for others to use. No need to reinvent the wheel right?')
st.caption('(instead of "spellbook" the technical term for the word after "import" is a **python library**)')
st.header("Python Libraries Used In This Page (the one you are literally reading right now):")
st.code('''
import streamlit as st
import pandas as pd
import os
import pathlib
import altair as alt
import streamlit.components.v1 as components
        ''')

st.divider()
st.header("Okay so, Soccer... and Data... *and* Science?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Hi I'm Coach Gus and I love soccer and physics. I enjoy teaching others about my passions and believe learning math and science does not have to be boring!")
        st.write("My favorite club team in England is :red[Liverpool FC] and I admire how their data science team combined physics knowledge with soccer knowledge to help the coaching staff better analyze the game.")
st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

col1, col2 = st.columns(2)
col1.write("They used their knowledge of charged particles and electric fields:")
col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
with col2:
        iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
        components.iframe(iframe_src2,600,500)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
        components.iframe(iframe_src,height=500)
        st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particles around")
st.subheader("The invention of the Pitch Control model helps coaches answer questions like:")
st.write(':orange["when is the right moment in the game to press and try to win the ball back?"]')
st.subheader("or")
st.write(':orange["in what areas of the field do our oppenents have a weakness we should attack?"]')

with st.expander("_The code for what you see above_", icon=":material/code:"):
    st.code(
          '''
st.header("Okay so, Soccer... and Data... *and* Science?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Hi I'm Coach Gus and I love soccer and physics. I enjoy teaching others about my passions and believe learning math and science does not have to be boring!")
        st.write("My favorite club team in England is :red[Liverpool FC] and I admire how their data science team combined physics knowledge with soccer knowledge to help the coaching staff better analyze the game.")
st.subheader("One of the biggest soccer clubs in the world, Liverpool FC, hired particle physicists to help improve their soccer team")

col1, col2 = st.columns(2)
col1.write("They used their knowledge of charged particles and electric fields:")
col2.write("And combined it with soccer data to create this (known as the Pitch Control model):")
with col2:
        iframe_src2 = "https://www.youtube.com/embed/Nc3uFWnPlsQ?si=pUx4ouf0EhWYMrVE"
        components.iframe(iframe_src2,600,500)

with col1:
        iframe_src = "https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_en.html"
        components.iframe(iframe_src,height=500)
        st.caption("Hint: make sure to click the 'Voltage' checkbox then drag and drop the red and blue particels around")
st.subheader("The invention of the Pitch Control model helps coaches answer questions like:")
st.write(':orange["when is the right moment in the game to press and try to win the ball back?"]')
st.subheader("or")
st.write(':orange["in what areas of the field do our oppenents have a weakness we should attack?"]')
'''
    )
st.divider()
st.header("What about that data thing? What *is* data?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Well first we collect information like: 'What are your hobbies? 'What is your favorite subject in school?' 'What is your favorite sport?' 'What kind of career(s) are intersting to you?'")
        st.write("and then we organize it!")
info = {
      'Name': ['Taylor','Kade','Gabe','Carolina','Kylie','Lucas','Teddy','Olivia','Alex','Dashley','Jameson','Evan','Kellan','Gregory'], 
      'Hobby':['soccer','soccer and basketball','soccer', 'swimming, playing basketball and reading.', 'soccer' ,'soccer, football, video games', 'soccer', 'soccer', 'soccer','soccer, cooking', 'soccer, musical theater','Art, Track, Soccer','Soccer and Legos', 'video game designer'], 
      'Favorite school subject': ['Math','Math','Math','Science','Science','Math','History','Math','Social Studies','Math','Social Studies','Math','History','History'], 
      'Favorite Sport': ['Soccer', 'Basketball', 'Soccer', 'Basketball/Tennis', 'Soccer', 'Football', 'Football', 'Soccer', 'Soccer', 'Soccer', 'Soccer','Soccer','Soccer','Soccer'], 
      'Year Born': ['2012','2012','2013','2014','2011','2012','2012','2012','2012','2013','2011','2013','2013','2013'], 
      'Career Interest':['Soccer','NBA player', 'Soccer', 'Veterinarian', 'Physical Therapy', 'Soccer', 'Soccer', 'Engineer, almost any type', 'Soccer', 'Soccer Player', 'Soccer, Architecture','Brain Surgery','History Teacher','Video Game Programmer']
      }

campers_db = pd.DataFrame(data=info)
st.dataframe(campers_db)
st.header("So, Data is a *Collection* of *Structured* *Information*")

with st.expander("_enter the matrix_", icon=":material/code:"):
      st.code('''
st.header("What about that data thing? What *is* data?")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Well first we collect information like: 'What are your hobbies? 'What is your favorite subject in school?' 'What is your favorite sport?' 'What kind of career(s) are intersting to you?'")
        st.write("and then we organize it!")
info = {
      'Name': ['Taylor','Kade','Gabe','Carolina','Kylie','Lucas','Teddy','Olivia','Alex','Dashley','Jameson'], 
      'Hobby':['soccer','soccer and basketball','soccer', 'swimming, playing basketball and reading.', 'soccer' ,'soccer, football, video games', 'soccer', 'soccer', 'soccer','soccer, cooking', 'soccer, musical theater'], 
      'Favorite school subject': ['Math','Math','Math','Science','Science','Math','History','Math','Social Studies','Math','Social Studies'], 
      'Favorite Sport': ['Soccer', 'Basketball', 'Soccer', 'Basketball/Tennis', 'Soccer', 'Football', 'Football', 'Soccer', 'Soccer', 'Soccer', 'Soccer'], 
      'Year Born': ['2012','2012','2013','2014','2011','2012','2012','2012','2012','2013','2011'], 
      'Career Interest':['Soccer','NBA player', 'Soccer', 'Veterinarian', 'Physical Therapy', 'Soccer', 'Soccer', 'Engineer, almost any type', 'Soccer', 'Soccer Player', 'Soccer, Architecture']
      }

campers_db = pd.DataFrame(data=info)
st.dataframe(campers_db)
st.header("So, Data is a *Collection* of *Structured* *Information*")
''')


st.divider()
with st.echo("below"):
        st.header("Okay, so I know what Soccer is but what do we mean by ''Data Science''?")
        st.image("./media/datascience.png")

st.header("Soccer Data Science")
coach_message = st.chat_message(name="Coach Gus",avatar="./media/profile_coachGus.JPG")
with coach_message:
        st.write("Looking back at the Venn Diagram above, Data Science is Hacking Skills + Substantive Expertise + Math & Statistics Knowledge ")
        st.write("Let's define these terms in our own words:")
        st.write(":red[**Hacking Skills**] = making the computer do stuff with code")
        st.write(":blue[**Substantive Expertise**] = Deep knowledge about a specific topic, like the game of soccer")
        st.write(":green[**Math and Statistics Knowledge**] = The ability to analyze things using mathematical tools")

        st.subheader('So Soccer Data Scientists ask questions like')
        st.subheader('"In 2023 who was the best attacker in MLS?"')
        st.subheader("They follow the scientific method, do math, write code, and learn that it is... Lionel Messi")
        #st.page_link("./coach/2_US_Pro_Soccer.py", label="Can you find an answer for this question?", icon="🤔")