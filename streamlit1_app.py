import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


# Insertar HTML personalizado
components.html("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", height=0, width=0)


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Nestor Carpio, Maestria en Gestion Estrategica
##### *Curriculum* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Mejora y Desarrollo de Procesos, con mas de 10 años de experiencia en Cadena de Suministro, Sistemas Informaticos, Financieros y Administrativos. 
- Desarrollo de Proyectos en toda la cadena de Empresa generando mejoras en el desarrollo organizacional por medio del uso de la tecnologia, y metodologias de cambio organizacional, Lean y Agiles
- Desarrollo de Proyectos de mejora y tecnologia utilizando herramientas y plataformas de sistemas en VBA, SQL, POO, Pyton, Streamlit, Analisis Estadistico, ML
''')

####################

# Navigation

#st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#st.markdown("""
#<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
#  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Nestor Carpio</a>
#  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#    <span class="navbar-toggler-icon"></span>
#  </button>
#  <div class="collapse navbar-collapse" id="navbarNav">
 #   <ul class="navbar-nav">
  #    <li class="nav-item active">
#     <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
 #     </li>
  #    <li class="nav-item">
  #      <a class="nav-link" href="#educacion">Educacion</a>
    #  </li>
     # <li class="nav-item">
       # <a class="nav-link" href="#Experiencia de Trabajo">Experiencia de Work</a>
      #</li>
#      <li class="nav-item">
  #      <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
  #    </li>
  #    <li class="nav-item">
   #     <a class="nav-link" href="#social-media">Social Media</a>
    #  </li>
    #</ul>
  #</div>
#</nav>
#""", unsafe_allow_html=True)

#st.markdown("""
#<nav style="background-color: #16A2CB; position: fixed; top: 0; width: 100%; z-index: 1000;">
 #<ul style="list-style-type: none; padding: 10px; display: flex; justify-content: space-around; margin: 0;">
    #<li><a style="text-decoration: none; color: white;" href="/">Home</a></li>
     #<li><a style="text-decoration: none; color: white;" href="#educacion">Educacion</a></li>
   #<li><a style="text-decoration: none; color: white;" href="#experiencia-de-trabajo">Experiencia de Trabajo</a></li>
   #<li><a style="text-decoration: none; color: white;" href="#herramientas-informaticas">Herramientas Informaticas </a></li>
   # <li><a style="text-decoration: none; color: white;" href="#social-media">Social Media</a></li>
 # </ul>
#</nav>
#""", unsafe_allow_html=True)

import streamlit as st

st.markdown("""
<nav style="background-color: #16A2CB; position: fixed; top: 0; width: 100%; z-index: 1000; padding: 10px; overflow-x: auto;">
  <ul style="list-style-type: none; padding: 0; margin: 0; display: flex; justify-content: flex-start; flex-wrap: nowrap; width: max-content;">
    <li><a style="text-decoration: none; color: white; margin-right: 10px;" href="/">Home</a></li>
    <li><a style="text-decoration: none; color: white; margin-right: 10px;" href="#educacion">Educacion</a></li>
    <li><a style="text-decoration: none; color: white; margin-right: 10px;" href="#experiencia-de-trabajo">Experiencia de Trabajo</a></li>
    <li><a style="text-decoration: none; color: white; margin-right: 10px;" href="#herramientas-informaticas">Herramientas Informaticas</a></li>
    <li><a style="text-decoration: none; color: white; margin-right: 50px;" href="#social-media">Social Media</a></li>
  </ul>
</nav>

<style>
/* Asegura que el contenido no quede oculto debajo del menú */
body {
    padding-top: 60px; /* Ajusta el valor según la altura de tu menú */
}

/* Añade un pequeño margen superior a las secciones */
section {
    margin-top: 10px; /* Ajusta este valor para mover las secciones hacia abajo */
}

""", unsafe_allow_html=True)










    
    
    




    
        












st.markdown('<a href="#top" style="text-decoration: none;">Inicio</a>', unsafe_allow_html=True)

st.markdown('<div id="top"></div>', unsafe_allow_html=True)



# Aquí puedes agregar más contenido.






#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Educacion
''')

txt('**Maestria en Gestion Estrategica** (Empresas), *Universidad Catolica*, El Salvador',
'2014-2017')
st.markdown('''
- GPA: `8.75`
- Tesis, Investigacion `El papel de la responsabilidad Social en las empresas: `.

''')

txt('**Licenciatura Administracion de Empresas** (Gestion Estrategica), *Universidad Modular*, El Salvador',
'2005-2010')
st.markdown('''

- Preespecializacion Gestion de la Calidad, Recursos Humanos, Desarrollo Gerencial.

- Certificacion Black Belt En Ingenieria de Procesos, *Green Consulting incorporated*, US', ' 2007-2008
''')

#####################
st.markdown('''
## Experiencia de trabajo
''')

txt('**Jefe Logistica, Sistemas de Inventario**, Finanzas Corporativas, Fruit Inc Balsamar, El Salvador',
'2009-2023')
st.markdown('''
- Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
- Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
- Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
- Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
''')

txt('**Associate Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
'2012-2021')
txt('**Assistant Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
'2009-2012')
txt('**Lecturer**, Faculty of Medical Technology, Mahidol University, Thailand',
'2006-2009')
st.markdown('''
- Provided mentorship and supervision to junior faculty, researchers, Ph.D./M.Sc./B.Sc. students. Mentored `3` Post-doctoral fellows, supervised `13` Ph.D. students, supervised `8` M.Sc. students, supervised `13` B.Sc. students and hosted `6` visiting students from U.S., Sweden and India.
- Wrote and applied for research grants. Served as Principal Investigator for research grants that have been awarded `12.5 million THB` and `1.117 million SEK` in research funding from Thai and Swedish grant agencies.
- Conducted research by applying machine learning to computational drug discovery and ensuring that research output exceeds `20+` articles per year.
- Taught `10+` undergraduate/graduate classes on Bioinformatics, Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
- Peer reviewed `100+` research articles for leading scientific journals.
''')

txt('**Co-Chair**, International Conference on Pharmaceutical Bioinformatics at Pattaya, Thailand',
'2016')
st.markdown('''
- Oversee all aspects of the conference preparations from conception to launch. This include inviting keynote and plenary speakers, create advertisement flyers, create abstract book, etc.
- Conference attracted `200+` participants from `40+` countries from university and industry sector.
- Chaired keynote session, technical workshop and some of the parallel sessions.
''')

txt('**Content Creator**, [Data Professor YouTube Channel](https://youtube.com/dataprofessor/)',
'2019-Present')
st.markdown('''
- `100,000+` subscribers on YouTube
- Created `261` educational videos on data science, machine learning and bioinformatics as well as hosted several podcast episodes with data scientists.
- Created `3` sponsored videos for Notion, Gradio and Classpert.
''')

txt('**Content Creator**, [Coding Professor YouTube Channel](https://youtube.com/codingprofessor/)',
'2019-Present')
st.markdown('''
- `3,200+` subscribers on YouTube
- Created `38` educational videos on Python and R programming.
''')

txt('**Technical Writer**, [Data Professor Blog](https://data-professor.medium.com/) on Medium.com',
'2019-Present')
st.markdown('''
- `4,100+` subscribers on Medium
- Written `68` technical blogs on data science, machine learning and bioinformatics.
''')

#####################
st.markdown('''
## Herramientas Informaticas
''')
txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/chaninn/')
txt2('', 'https://github.com/chaninlab/')
txt2('', 'https://github.com/dataprofessor')
txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
txt2('Publons', 'https://publons.com/a/303133/')
