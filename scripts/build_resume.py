from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from pathlib import Path
root=Path(__file__).resolve().parents[1]
navy=colors.HexColor('#10243e');teal=colors.HexColor('#087e79')
styles={
 'name':ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=22,leading=25,textColor=navy,spaceAfter=4),
 'title':ParagraphStyle('title',fontName='Helvetica-Bold',fontSize=10,leading=13,textColor=teal,spaceAfter=5),
 'contact':ParagraphStyle('contact',fontName='Helvetica',fontSize=8.5,leading=12,spaceAfter=9),
 'section':ParagraphStyle('section',fontName='Helvetica-Bold',fontSize=9,leading=12,textColor=teal,spaceBefore=9,spaceAfter=4),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=9.4,leading=12.5,spaceAfter=5),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=8.6,leading=11.5,spaceAfter=4)
}
def link(url,label):return f'<a href="{url}" color="#174e83"><u>{label}</u></a>'
story=[]
def p(t,style='body'):story.append(Paragraph(t,styles[style]))
p('RAYMOND ANTHONY GOMEZ','name')
p('AI PROTOTYPE BUILDER | PRODUCT DISCOVERY | DECISION SUPPORT','title')
p('Orchard Park, New York | (716) 697-5928 | '+link('mailto:rayoonbaco@yahoo.com','rayoonbaco@yahoo.com')+'<br/>'+link('https://the-receipts.onrender.com/','The Receipts: portfolio')+' &nbsp; | &nbsp; '+link('https://www.linkedin.com/in/ray-gomez-20b80342/','LinkedIn')+' &nbsp; | &nbsp; '+link('https://github.com/rayoonbaco','GitHub'),'contact')
p('BUILDER PROFILE','section')
p('AI-assisted product builder with 18+ years of business experience translating complex questions into practical decision support. I investigate unfamiliar problems, define useful prototypes, direct AI-assisted implementation, test failure modes and publish inspectable evidence. Seeking a paid role or project with a team building practical AI tools.')
p('SELECTED BUILDS & COMPETITION EXPERIENCE','section')
p('<b>Housing Navigator | Solo Global AI Hackathon submission | October 2026</b><br/>Hack-Nation 7th Global AI Hackathon, RealPage challenge; participated at the Carnegie Mellon hub. '+link('https://housing-navigator.onrender.com/','Working demo')+' | '+link('https://github.com/rayoonbaco/Housing_Navigator','Source and evidence'))
p('Built an address-and-date housing-rule prototype with six resident questions and a “Check my homework” evidence view. The documented release contains 310 rules and 500 addresses across four dates; repository records include 72 offline engine tests. Preserved unknown facts, source gaps and failed checks. Saved-result prototype, not legal advice.','small')
p('<b>Artificial Stupidity | Evidence-gated AI research prototype</b> | '+link('https://artificial-stupidity.onrender.com/','Demo')+' | '+link('https://github.com/rayoonbaco/artificial-stupidity','Repository'))
p('Built a KEEP, REJECT or ESCALATE authorization boundary separating AI proposals from acceptance. Published holdouts, provenance, failed tests and repairs; documented a 74-test CPU suite and an H100-backed experiment. Bounded research prototype, not a general AI-safety certification.','small')
p('<b>Bill X-Ray | Legislative decision intelligence</b> | '+link('https://bill-xray-uapi.onrender.com/','Demo')+'<br/>Turns dense legislation into plain-English decision support with evidence links, adversarial review, uncertainty and a Check My Homework layer.','small')
p('<b>Monahinga HUNTER | Geospatial decision support</b> | '+link('https://monahinga-hunter.onrender.com/','Demo')+'<br/>Combines elevation data, 2D/3D terrain, land context, routing and explainable scoring for human field review.','small')
p('BUILD PRACTICE','section')
p('<b>Independent AI Product Builder and Decision-Systems Prototyper</b> | Self-directed | Oct 2025-present<br/>Research and ship web applications and decision tools using ChatGPT, Claude, Codex, GitHub, Python, JSON and cloud deployment. Define the user decision, compare solution approaches, pressure-test evidence, build, evaluate and document limitations. Portfolio includes Flood Action Lens, Scout Horizon, Invisible Air Observatory and AI Draft Buddy.')
p('PRIOR BUSINESS EXPERIENCE','section')
p('<b>Senior Financial Reporting Analyst</b>, Nissha Medical Technologies | Jul 2023-May 2024<br/><b>Associate Manager, Sales Reporting</b>, Ivoclar Vivadent | Feb 2014-Jul 2023<br/><b>Senior Financial Analyst</b>, Ivoclar Vivadent | Feb 2005-Feb 2014','small')
p('Built reporting, forecasting, profitability, scenario and decision-support systems; translated stakeholder questions and changing data into practical tools and executive insight.','small')
p('EDUCATION & CAPABILITIES','section')
p('<b>BS, Business Administration</b>, University of Louisville | University at Buffalo School of Management Data Modeling Program | 28 applied-AI certificates','small')
p('Product discovery; research synthesis; rapid prototyping; prompt and system design; AI-agent orchestration; evidence grounding; adversarial evaluation; GitHub; Python; JSON; Excel; Power Query; geospatial visualization.','small')
doc=SimpleDocTemplate(str(root/'Ray_Gomez_AI_Builder_Resume.pdf'),pagesize=(612,792),rightMargin=38,leftMargin=38,topMargin=30,bottomMargin=30,title='Ray Gomez - AI Prototype Builder',author='Raymond Anthony Gomez')
doc.build(story)
