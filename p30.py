import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")

st.title("vetenary Decision support App")
st.write("Enter Milk production based hard health analysis")

st.sidebar.title("farm settings")

#NUMBER OF COWS

cow_count = st.sidebar.number_input("Enter Number of cows",
    min_value =1,
    max_value =50,
    value =3
)
#milk input

milk_values = []
temp_values= []
feed_values = []
cow_names = []

st.subheader(" milk production ")

for i in range(cow_count):
    st.markdown(f"### cow {i+1}")
    cow_name = st.text_input(f"enter cow{i+1}name",key=f"{i}"
    )                         
                
    milk = st.number_input(f"cow {i+1} Milk production",
                           min_value=0.0,
                           step=0.5,
                           key=f"milk{i}"
    )

    temp = st.number_input(f"cow {i+1} body temperature(F)",                           min_value=90.0,
                           max_value=110.0,
                           step=0.1,
                           value=101.5,
                           key=f"temp{i}"
                           
    )

    feed = st.slider("feed intake",                          
                           0,
                           100,
                           50,
                           key=f"feed{i}"
                     
   )
    
    cow_names.append(cow_name if cow_name else f"cow{i+1}")               
    milk_values.append(milk)
    temp_values.append(temp)
    feed_values.append(feed)
               

#analyze button

if st.button("Analyze health"):

    y= np.array(milk_values)

    x= np.arange(len(y))
    avg_milk = np.mean(y)           

    


                     
#health analysis

   # avg_milk = np.mean(y)
    st.subheader("health analysis result")

    st.write(f"average milk production:{avg_milk:.2f}liters")

#check each cow

    for i, milk in enumerate(y):

        st.write(f"cow name:{cow_names[i]}")
        st.write(f"(milk production:{milk}")       
        st.write(f"(temperature:{temp_values[i]}")
        st.write(f"feed intake:{feed_values[i]}")
               
        if milk < avg_milk * 0.5:

            st.error(f"cow{i+1}:severe milk drop detected")

            st.write("possible causes")
            st.write("mastitis risk")
            st.write("nutrition Deficiency")

        elif milk < avg_milk * 0.8:

                st.warning(f"cow{i+1}:moderate milk detected")

                st.write("possible cause")
                st.write("early infection")
                st.write("heat stress")
                st.write ("feed imbalance")

        else:

               st.success(f"cow{1+1}:normal milk production")

               if temp_values[i] >103:
                  st.warning(" high fever detected")
                  
               if feed_values[i] < 30:
                  st.warning(" low feed intake")
                  

                    

#final summary
#if st.button("analyze health"):
              
avg_milk = sum(milk_values)/len(milk_values)
y = np.array(milk_values)            
         
st.subheader("final summary")
if min(y) < avg_milk * 0.5:
    st.error(" high risk animal detected")
elif min(y) < avg_milk * 0.8:
    st.warning("some cows need monitoring ")
else:
     st.success("farm condition looks normal")
                     

                     
                     
    
                            


 


