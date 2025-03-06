import streamlit as st
from PIL import Image
import pandas as pd
import base64
from io import BytesIO
import time

st.set_page_config(
    page_title="Aime Claudien Mazimpaka - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Base Styles and Typography */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary: #ff3333;
        --primary-light: #ff3333;
        --secondary: #ff3333;
        --accent: #f72585;
        --dark: #000;
        --light: #f8f9fa;
        --gray: #6c757d;
        --success: #4cc9f0;
        --warning: #f8961e;
        --danger: #ff3333;
        --gradient: linear-gradient(120deg, var(--primary), var(--secondary));
    }
    
    .main {
        padding: 2rem;
        font-family: 'Poppins', sans-serif;
        color: #333;
    }
            
    .project-description {
        font-size: 1.2rem;
        font-weight: 400;
        color: var(--dark);
        margin-bottom: 1rem;
    }
            
    .achievement-text {
        font-size: 1.2rem;
        font-weight: 400;
        color: var(--dark);
        margin-bottom: 1rem;
    }
    
    .title-text {
        font-size: 3rem;
        font-weight: 700;
        background: var(--gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .subtitle-text {
        font-size: 1.5rem;
        color: var(--gray);
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Section Titles */
    .section-title {
        font-size: 2rem;
        font-weight: 600;
        color: var(--primary);
        padding-bottom: 0.75rem;
        position: relative;
        margin-bottom: 2rem;
        margin-top: 2.5rem;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: 0;
        height: 4px;
        width: 60px;
        background: var(--gradient);
        border-radius: 2px;
    }
    
    /* Cards and Containers */
    .project-card {
        background-color: white;
        border-radius: 1rem;
        padding: 1.75rem;
        margin-bottom: 1.75rem;
        border: none;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--gradient);
        opacity: 0.7;
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(67, 97, 238, 0.1);
    }
    
    .project-card h3 {
        color: var(--dark);
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Skill Bars */
    .skill-container {
        margin-bottom: 1.5rem;
    }
    
    .skill-name {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .skill-percent {
        color: var(--primary);
        font-weight: 600;
    }
    
    .skill-bar {
        height: 10px;
        background: #e9ecef;
        border-radius: 5px;
        overflow: hidden;
    }
    
    .skill-progress {
        height: 100%;
        background: var(--gradient);
        border-radius: 5px;
        position: relative;
        transition: width 1.5s ease-in-out;
    }
    
    /* Timeline */
    .timeline-item {
        padding: 1.5rem;
        border-left: 3px solid var(--primary);
        margin-left: 1.5rem;
        margin-bottom: 1.5rem;
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -10px;
        top: 2rem;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: white;
        border: 3px solid var(--primary);
    }
    
    .timeline-year {
        display: inline-block;
        background: var(--primary-light);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 2rem;
        font-size: 0.9rem;
        margin-bottom: 0.75rem;
    }
    
    /* Testimonials */
    .testimonial-card {
        background-color: white;
        border-radius: 1rem;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        position: relative;
    }
    
    .testimonial-card::before {
        content: '\\201C';
        font-family: Georgia, serif;
        position: absolute;
        top: 10px;
        left: 20px;
        font-size: 5rem;
        color: rgba(67, 97, 238, 0.1);
        line-height: 1;
    }
    
    .testimonial-text {
        font-style: italic;
        margin-bottom: 1.5rem;
        padding-left: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .testimonial-author {
        display: flex;
        align-items: center;
    }
    
    .testimonial-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: var(--gradient);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        margin-right: 1rem;
    }
    
    /* Contact Form */
    .contact-form {
        background-color: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    
    .contact-form input, .contact-form textarea {
        border: 1px solid #e9ecef;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1.5rem;
        transition: border-color 0.3s, box-shadow 0.3s;
    }
    
    .contact-form input:focus, .contact-form textarea:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.1);
        outline: none;
    }
    
    /* Social Links */
    .social-links {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1.5rem;
    }
    
    .social-link {
        background: var(--gradient);
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        transition: transform 0.3s, box-shadow 0.3s;
        font-weight: 500;
        box-shadow: 0 5px 15px rgba(67, 97, 238, 0.2);
        text-decoration: none;
        color: var(--light);
    }
    
    .social-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(67, 97, 238, 0.3);
        color: white;
    }
    
    .social-link i {
        font-size: 1.2rem;
        color: white;
    }
    
    /* Animations */
    .fade-in {
        animation: fadeIn 0.8s ease-out;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .slide-in {
        animation: slideIn 0.8s ease-out;
    }
    
    @keyframes slideIn {
        0% { opacity: 0; transform: translateX(-30px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    
    /* Icons */
    .icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        margin-right: 0.5rem;
        color: var(--primary);
    }
    
    .icon-large {
        width: 40px;
        height: 40px;
        font-size: 1.5rem;
    }
    
    .icon-circle {
        background: rgba(67, 97, 238, 0.1);
        border-radius: 50%;
        padding: 0.75rem;
    }
    
    /* Custom Sidebar */
    .sidebar .sidebar-content {
        background: white;
        border-right: none;
    }
    
    /* Stats Cards */
    .stats-card {
        background: white;
        border-radius: 1rem;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        transition: transform 0.3s;
    }
    
    .stats-card:hover {
        transform: translateY(-5px);
    }
    
    .stats-icon {
        width: 60px;
        height: 60px;
        background: rgba(67, 97, 238, 0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        color: var(--primary);
        margin-right: 1rem;
    }
    
    .stats-info h4 {
        font-weight: 600;
        margin-bottom: 0.25rem;
        color: var(--dark);
    }
    
    .stats-info p {
        color: var(--gray);
        font-size: 1.25rem;
        font-weight: 500;
    }
    
    /* Achievement Items */
    .achievement-item {
        padding: 1rem;
        border-radius: 0.5rem;
        background: white;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        transition: transform 0.3s;
    }
    
    .achievement-item:hover {
        transform: translateX(5px);
    }
    
    .achievement-icon {
        min-width: 40px;
        height: 40px;
        background: var(--primary-light);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        margin-right: 1rem;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .title-text {
            font-size: 2.25rem;
        }
        
        .subtitle-text {
            font-size: 1.25rem;
        }
        
        .section-title {
            font-size: 1.75rem;
        }
        
        .social-links {
            flex-direction: column;
        }
    }
</style>

<!-- Icon Library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
""", unsafe_allow_html=True)

if 'name' not in st.session_state:
    st.session_state['name'] = "Aime Claudien Mazimpaka"
if 'location' not in st.session_state:
    st.session_state['location'] = "Kigali, Rwanda"
if 'university' not in st.session_state:
    st.session_state['university'] = "Ines Ruhengeri University"
if 'field' not in st.session_state:
    st.session_state['field'] = "Bachelor's Degree in Software Engineering (Graduation: Sept 2025)"
if 'bio' not in st.session_state:
    st.session_state['bio'] = "Dedicated and detail-oriented Software Engineering student with strong expertise in front-end and back-end development. Proficient in React, HTML, CSS, JavaScript, PHP, Java, and Python, with hands-on experience in developing business management systems. Passionate about leveraging technology to create innovative and efficient solutions."
if 'profile_pic' not in st.session_state:
    st.session_state['profile_pic'] = None
if 'resume' not in st.session_state:
    # Load default resume (cv.pdf)
    try:
        with open("cv.pdf", "rb") as file:
            default_resume = BytesIO(file.read())
            st.session_state['resume'] = default_resume
    except Exception as e:
        st.session_state['resume'] = None
if 'skills' not in st.session_state:
    st.session_state['skills'] = {
        "JavaScript": 85,
        "Java": 80,
        "Python": 75,
        "SQL": 80,
        "React.js": 85,
        "Bootstrap": 90,
        "Tailwind CSS": 85,
        "HTML/CSS": 90,
        "PHP": 80,
        "Laravel": 75,
        "Next.js": 70,
        "Node.js": 75,
        "Git/GitHub": 85
    }
if 'achievements' not in st.session_state:
    st.session_state['achievements'] = [
        "Developed multiple business portfolio websites for clients",
        "Created a Windows Student Management System",
        "Designed and implemented E-commerce and E-learning platforms",
        "Developed a Lost and Found System as a freelance project",
        "Created an online Ticket Booking System as a freelance project",
        "Designed an online Voting System for organizations"
    ]

if 'menu' not in st.session_state:
    st.session_state['menu'] = "Home"

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
<style>    
    .nav-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff;
        padding: 1rem 0;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #f0f0f0;
        text-align: center;
    }
    
    .nav-item {
        display: flex;
        align-items: center;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #fff;
        text-decoration: none;
        position: relative;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .nav-item:hover {
        background-color: rgba(240, 244, 248, 0.15);
        color: #4cc9f0;
        transform: translateX(3px);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
    }
    
    .nav-item.active {
        background-color: rgba(232, 240, 254, 0.2);
        color: var(--primary);
        font-weight: 600;
        border-left: 3px solid var(--success);
        box-shadow: 0 2px 8px rgba(76, 201, 240, 0.3);
    }
    
    .nav-icon {
        margin-right: 12px;
        width: 24px;
        text-align: center;
        font-size: 1.1rem;
    }
    
    .nav-text {
        font-size: 1rem;
    }
    
    /* Subtle animation for the active indicator */
    .nav-item.active::before {
        content: "";
        position: absolute;
        left: 0;
        width: 4px;
        height: 100%;
        background-color: var(--success);
        transform: translateX(-2px);
    }
    
    /* Add ripple effect */
    .nav-item::after {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        width: 5px;
        height: 5px;
        background: rgba(255, 255, 255, 0.5);
        opacity: 0;
        border-radius: 100%;
        transform: scale(1, 1) translate(-50%, -50%);
        transform-origin: 50% 50%;
    }
    
    .nav-item:focus:not(:active)::after {
        animation: ripple 1s ease-out;
    }
    
    @keyframes ripple {
        0% {
            transform: scale(0, 0);
            opacity: 0.5;
        }
        20% {
            transform: scale(25, 25);
            opacity: 0.3;
        }
        100% {
            opacity: 0;
            transform: scale(40, 40);
        }
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="nav-title">Navigation</div>', unsafe_allow_html=True)
    
    # Define menu options
    menu_options = [
        "Home",
        "Projects", 
        "Skills & Achievements", 
        "Timeline", 
        "Testimonials", 
        "Contact", 
        "Customize Profile"
    ]
    
    # Create buttons for each menu option
    for option in menu_options:
        # Determine if this is the active menu
        is_active = option == st.session_state['menu']
        
        # Set button style based on active state
        button_type = "primary" if is_active else "secondary"
        
        # Create the button
        if st.button(option, key=f"nav_{option.lower().replace(' & ', '_').replace(' ', '_')}", 
                    use_container_width=True, type=button_type):
            st.session_state['menu'] = option
            st.rerun()
    
    # Add CSS for styling the navigation
    st.markdown("""
    <style>
    .nav-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        color: var(--success);
    }
    
    /* Style the buttons to look like navigation items */
    .stButton button {
        display: flex;
        align-items: center;
        width: 100%;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: left;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    /* Primary button (active) */
    .stButton button[data-testid="baseButton-primary"] {
        background-color: rgba(232, 240, 254, 0.2) !important;
        color: var(--success) !important;
        font-weight: 600 !important;
        border-left: 3px solid var(--success) !important;
        box-shadow: 0 2px 8px rgba(76, 201, 240, 0.3) !important;
        border-color: transparent !important;
    }
    
    /* Secondary button (inactive) */
    .stButton button[data-testid="baseButton-secondary"] {
        background-color: transparent !important;
        color: white !important;
        border-color: transparent !important;
    }
    
    .stButton button[data-testid="baseButton-secondary"]:hover {
        background-color: rgba(240, 244, 248, 0.15) !important;
        color: #4cc9f0 !important;
        transform: translateX(3px);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15) !important;
    }
    </style>
    """, unsafe_allow_html=True)

current_menu = st.session_state['menu']


def get_download_link(file, filename):
    """Generate a download link for the resume file"""
    b64 = base64.b64encode(file.getvalue()).decode()
    
    # Generate a unique ID for this link
    link_id = f"download-link-{hash(filename) % 10000}"
    
    href = f'''
    <style>
        #{link_id}:hover {{
            background-color: var(--primary-light) !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }}
    </style>
    <a id="{link_id}" 
       href="data:application/octet-stream;base64,{b64}" 
       download="{filename}" 
       class="social-link" 
       style="display: inline-flex; align-items: center; margin-top: 1rem; background-color: var(--primary); color: white; padding: 0.5rem 1rem; border-radius: 4px; text-decoration: none; transition: all 0.3s ease;">
        <i class="fas fa-file-pdf" style="margin-right: 0.5rem;"></i> Download Resume
    </a>
    '''
    return href

def filter_projects(projects, category):
    if category == "All Projects":
        return projects
    return [p for p in projects if category in p["categories"]]

projects = [
    {
        "title": "Business Portfolio Websites",
        "type": "Client Project",
        "year": "2023-2024",
        "description": "Designed and developed professional portfolio websites to showcase businesses, services, and projects, integrating responsive design for better user accessibility. Examples include Ikigugu Group and Virunga Homestay.",
        "link": "https://ikigugugroup.rw/ |  https://virungahomestay.com/",
        "categories": ["Web Development", "Client Projects", "Portfolio"]
    },
    {
        "title": "Student Management System",
        "type": "Windows Application",
        "year": "2023",
        "description": "Developed a comprehensive Windows-based system for managing student records, attendance, grades, and other academic information.",
        "link": "https://github.com/Aimecol/StudentManagement-System.git",
        "categories": ["Desktop Applications", "Education", "Management Systems"]
    },
    {
        "title": "E-commerce System",
        "type": "Web Application",
        "year": "2024",
        "description": "Designed and implemented an online shopping platform with product management, secure payment integration, and a user-friendly interface to enhance the shopping experience.",
        "link": "#",
        "categories": ["Web Development", "E-commerce", "Full Stack"]
    },
    {
        "title": "E-learning System",
        "type": "Web Application",
        "year": "2024",
        "description": "Created an interactive platform for online education with course management, student tracking, and content delivery features.",
        "link": "https://aimecol.github.io/E-learnPro/",
        "categories": ["Web Development", "Education", "Full Stack"]
    },
    {
        "title": "Real Estate System",
        "type": "Web Application",
        "year": "2024",
        "description": "Developed a property listing and management platform for real estate businesses, featuring property search, filtering, and inquiry management.",
        "link": "https://aimecol.github.io/Estate/RealEastatePro/",
        "categories": ["Web Development", "Real Estate", "Full Stack"]
    },
    {
        "title": "Lost and Found System",
        "type": "Freelance Project",
        "year": "2024",
        "description": "Designed a system for users to report lost items and search for found items; featured a verification mechanism to ensure rightful ownership.",
        "link": "#",
        "categories": ["Freelance", "Web Applications", "Community Services"]
    },
    {
        "title": "Ticket Booking System",
        "type": "Freelance Project",
        "year": "2024",
        "description": "Created an online ticket booking platform where users can select events, book seats, and make payments securely.",
        "link": "#",
        "categories": ["Freelance", "Web Applications", "E-commerce"]
    },
    {
        "title": "Voting System",
        "type": "Web Application",
        "year": "2024",
        "description": "Developed an online voting system with reliable authentication, ensuring transparency and security in elections for organizations and institutions.",
        "link": "#",
        "categories": ["Web Applications", "Security", "Community Services"]
    },
    {
        "title": "Advanced Blood Donation System",
        "type": "Ongoing Project",
        "year": "2025",
        "description": "Currently developing a comprehensive system to manage blood donation processes, donor records, and inventory management for blood banks.",
        "link": "#",
        "categories": ["Ongoing", "Web Applications", "Healthcare"]
    }
]

testimonials = [
    {
        "text": "Aime is a dedicated professional who delivered an excellent business portfolio website for our company. His attention to detail and technical skills are impressive.",
        "author": "Munyentwari Clement",
        "position": "CEO/Software Engineer at Ikigugu Group Ltd"
    },
    {
        "text": "Working with Aime was a great experience. He understood our requirements perfectly and delivered quality services for our business needs.",
        "author": "Bucyimanibaruta Gustave",
        "position": "CEO at PEDA Ltd"
    }
]

timeline = [
    {
        "year": "2020-2021",
        "event": "Hardware Store Owner",
        "description": "Provided Rwandan e-services, clothing printing, bank, mobile, and Irembo services in Kigali-Kinamba-Gakinjiro."
    },
    {
        "year": "2021-2022",
        "event": "Service Provider at PEDA Ltd",
        "description": "Provided e-services, financial services, and printing solutions in Kayonza-Kabarondo. Assisted in streamlining operational workflows for business services as manager."
    },
    {
        "year": "2022",
        "event": "Started Software Engineering Degree",
        "description": "Began academic journey at Ines Ruhengeri University, focusing on software engineering fundamentals."
    },
    {
        "year": "2023-2024",
        "event": "Business Portfolio Websites",
        "description": "Developed professional websites for businesses including Ikigugu Group and Virunga Homestay."
    },
    {
        "year": "2024-2025",
        "event": "Freelance Software Development",
        "description": "Worked on various freelance projects including Lost and Found System, Ticket Booking System, and other web applications."
    },
    {
        "year": "2025",
        "event": "Advanced Blood Donation System",
        "description": "Currently developing a comprehensive system for managing blood donation processes and inventory."
    }
]

if current_menu == "Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if st.session_state['profile_pic']:
            st.image(st.session_state['profile_pic'], width=250)
        else:
            st.image("Aime.png", width=250)
            
        st.markdown('''
        <div class="social-links">
            <a href="https://github.com/Aimecol" target="_blank" class="social-link">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="mailto:aimecol314@gmail.com" class="social-link">
                <i class="far fa-envelope"></i> Email
            </a>
            <a href="tel:+250789375245" class="social-link">
                <i class="fas fa-phone-alt"></i> Call
            </a>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="title-text fade-in">{st.session_state["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="subtitle-text fade-in">{st.session_state["field"]}</div>', unsafe_allow_html=True)
        
        st.markdown(f'''
        <div style="margin-bottom: 1.5rem;">
            <p style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span class="icon"><i class="fas fa-map-marker-alt"></i></span>
                <strong>Location:</strong> {st.session_state['location']}
            </p>
            <p style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span class="icon"><i class="fas fa-graduation-cap"></i></span>
                <strong>University:</strong> {st.session_state['university']}
            </p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div style="margin-bottom: 1.5rem;">
            <h3 style="display: flex; align-items: center; color: var(--primary); font-weight: 600;">
                <span class="icon"><i class="fas fa-user"></i></span> About Me
            </h3>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown(f"{st.session_state['bio']}")
        
        if st.session_state['resume']:
            # Check if this is the default resume
            is_default = False
            try:
                with open("cv.pdf", "rb") as file:
                    default_content = file.read()
                    current_content = st.session_state['resume'].getvalue()
                    is_default = default_content == current_content
            except:
                pass
                
            # Add a label if using default resume
            if is_default:
                st.markdown(get_download_link(st.session_state['resume'], "cv.pdf"), unsafe_allow_html=True)
                st.markdown('''
                <div style="margin-top: 0.5rem; font-size: 0.8rem; color: var(--gray);">
                    Download my resume.
                </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(get_download_link(st.session_state['resume'], "Resume.pdf"), unsafe_allow_html=True)
        else:
            st.markdown('''
            <button disabled class="social-link" 
                    style="display: inline-flex; align-items: center; margin-top: 1rem; background-color: var(--gray); 
                           color: white; padding: 0.5rem 1rem; border-radius: 4px; text-decoration: none; 
                           transition: all 0.3s ease; border: none; cursor: not-allowed; opacity: 0.7;">
                <i class="fas fa-file-pdf" style="margin-right: 0.5rem;"></i> Download Resume (Demo)
            </button>
            ''', unsafe_allow_html=True)
            
            st.markdown('''
            <div style="margin-top: 0.5rem; font-size: 0.8rem; color: var(--gray);">
                Upload a resume in the "Customize Profile" section to enable this button.
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Quick Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-laptop-code"></i>
            </div>
            <div class="stats-info">
                <h4>Projects</h4>
                <p>9 completed</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-trophy"></i>
            </div>
            <div class="stats-info">
                <h4>Achievements</h4>
                <p>{len(st.session_state['achievements'])}</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'''
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-code"></i>
            </div>
            <div class="stats-info">
                <h4>Tech Skills</h4>
                <p>{len(st.session_state['skills'])}</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)

elif current_menu == "Projects":
    st.markdown('<div class="section-title fade-in">My Projects</div>', unsafe_allow_html=True)
    
    project_categories = ["All Projects", "Web Development", "Client Projects", "Portfolio", "Desktop Applications", "Education", "Management Systems", "Freelance", "Web Applications", "Community Services", "E-commerce", "Security", "Healthcare", "Ongoing"]
    
    st.markdown('''
    <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
        <span class="icon"><i class="fas fa-filter"></i></span>
        <strong>Filter projects:</strong>
    </div>
    ''', unsafe_allow_html=True)
    
    selected_category = st.selectbox("", project_categories, label_visibility="collapsed")
    
    filtered_projects = filter_projects(projects, selected_category)
    
    if not filtered_projects:
        st.write("No projects match the selected filter.")
    else:
        for project in filtered_projects:
            icon_class = "fas fa-laptop-code"  
            
            if "Web Development" in project["categories"]:
                icon_class = "fas fa-globe"
            elif "Desktop Applications" in project["categories"]:
                icon_class = "fas fa-desktop"
            elif "E-commerce" in project["categories"]:
                icon_class = "fas fa-shopping-cart"
            elif "Healthcare" in project["categories"]:
                icon_class = "fas fa-heartbeat"
            elif "Education" in project["categories"]:
                icon_class = "fas fa-graduation-cap"
            elif "Security" in project["categories"]:
                icon_class = "fas fa-shield-alt"
            
            with st.container():
                st.markdown(f'''
                <div class="project-card fade-in">
                    <h3 style="display: flex; align-items: center;">
                        <span class="icon"><i class="{icon_class}"></i></span>
                        {project['title']}
                    </h3>
                    <p style="color: var(--gray); margin-bottom: 1rem;">
                        <span style="display: inline-flex; align-items: center; margin-right: 1rem;">
                            <i class="fas fa-tag" style="margin-right: 0.5rem;"></i> {project['type']}
                        </span>
                        <span style="display: inline-flex; align-items: center;">
                            <i class="far fa-calendar-alt" style="margin-right: 0.5rem;"></i> {project['year']}
                        </span>
                    </p>
                    <p class="project-description">{project['description']}</p>
                    <a href="{project['link']}" target="_blank" class="social-link" style="display: inline-flex; margin-top: 1rem; width: fit-content;">
                        <i class="fab fa-github"></i> View Code
                    </a>
                </div>
                ''', unsafe_allow_html=True)
    

elif current_menu == "Skills & Achievements":
    st.markdown('<div class="section-title fade-in"><i class="fas fa-code" style="margin-right: 0.5rem;"></i>Technical Skills</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    skills = list(st.session_state['skills'].items())
    half = len(skills) // 2
    
    def get_skill_icon(skill_name):
        skill_icons = {
            "JavaScript": "fab fa-js",
            "Java": "fab fa-java",
            "Python": "fab fa-python",
            "SQL": "fas fa-database",
            "React.js": "fab fa-react",
            "Bootstrap": "fab fa-bootstrap",
            "Tailwind CSS": "fab fa-css3",
            "HTML/CSS": "fab fa-html5",
            "PHP": "fab fa-php",
            "Laravel": "fab fa-laravel",
            "Next.js": "fab fa-react",
            "Node.js": "fab fa-node-js",
            "Git/GitHub": "fab fa-git-alt",
        }
        return skill_icons.get(skill_name, "fas fa-code")
    
    with col1:
        for skill, level in skills[:half]:
            icon_class = get_skill_icon(skill)
            st.markdown(f'''
            <div class="skill-container">
                <div class="skill-name">
                    <span style="display: flex; align-items: center;">
                        <i class="{icon_class}" style="margin-right: 0.5rem;"></i>
                        <strong>{skill}</strong>
                    </span>
                    <span class="skill-percent">{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
    
    with col2:
        for skill, level in skills[half:]:
            icon_class = get_skill_icon(skill)
            st.markdown(f'''
            <div class="skill-container">
                <div class="skill-name">
                    <span style="display: flex; align-items: center;">
                        <i class="{icon_class}" style="margin-right: 0.5rem;"></i>
                        <strong>{skill}</strong>
                    </span>
                    <span class="skill-percent">{level}%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {level}%;"></div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title fade-in"><i class="fas fa-trophy" style="margin-right: 0.5rem;"></i>Certifications & Achievements</div>', unsafe_allow_html=True)
    
    for i, achievement in enumerate(st.session_state['achievements']):
        st.markdown(f'''
        <div class="achievement-item">
            <div class="achievement-icon">
                <i class="fas fa-award"></i>
            </div>
            <div class="achievement-text">{achievement}</div>
        </div>
        ''', unsafe_allow_html=True)

elif current_menu == "Timeline":
    st.markdown('<div class="section-title fade-in"><i class="fas fa-history" style="margin-right: 0.5rem;"></i>Academic & Project Timeline</div>', unsafe_allow_html=True)
    
    def get_timeline_icon(event_name):
        if "Software" in event_name:
            return "fas fa-laptop-code"
        elif "University" in event_name or "Degree" in event_name:
            return "fas fa-graduation-cap"
        elif "Manager" in event_name or "Owner" in event_name:
            return "fas fa-briefcase"
        elif "Website" in event_name:
            return "fas fa-globe"
        elif "System" in event_name:
            return "fas fa-cogs"
        elif "Freelance" in event_name:
            return "fas fa-code"
        else:
            return "fas fa-star"
    
    for item in timeline:
        icon_class = get_timeline_icon(item['event'])
        st.markdown(f'''
        <div class="timeline-item fade-in">
            <span class="timeline-year">{item['year']}</span>
            <h4 style="display: flex; align-items: center; margin-top: 0.5rem; color: var(--dark);">
                <span class="icon"><i class="{icon_class}"></i></span>
                {item['event']}
            </h4>
            <p style="display: flex; align-items: center; margin-top: 0.5rem; color: var(--dark);">{item['description']}</p>
        </div>
        ''', unsafe_allow_html=True)

elif current_menu == "Testimonials":
    st.markdown('<div class="section-title fade-in"><i class="fas fa-comment-dots" style="margin-right: 0.5rem;"></i>What Others Say About Me</div>', unsafe_allow_html=True)
    
    for testimonial in testimonials:
        initials = ''.join([name[0] for name in testimonial['author'].split() if name])
        
        st.markdown(f'''
        <div class="testimonial-card fade-in">
            <p class="testimonial-text" style="color: var(--dark);">{testimonial['text']}</p>
            <div class="testimonial-author">
                <div class="testimonial-avatar">{initials}</div>
                <div>
                    <strong style="color: var(--dark);">{testimonial['author']}</strong>
                    <div style="color: var(--gray); font-size: 0.9rem;">
                        <i class="fas fa-briefcase" style="margin-right: 0.5rem;"></i>
                        {testimonial['position']}
                    </div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

elif current_menu == "Contact":
    st.markdown('<div class="section-title fade-in"><i class="fas fa-paper-plane" style="margin-right: 0.5rem;"></i>Get In Touch</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="contact-form">', unsafe_allow_html=True)
        st.markdown('''
        <h3 style="display: flex; align-items: center; margin-bottom: 1.5rem;">
            <i class="fas fa-envelope" style="margin-right: 0.75rem; color: var(--primary);"></i>
            Send Me a Message
        </h3>
        ''', unsafe_allow_html=True)
        
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        if st.button("Send Message"):
            st.success("Message sent successfully! (Demo only)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <h3 style="display: flex; align-items: center; margin-bottom: 1.5rem;">
            <i class="fas fa-link" style="margin-right: 0.75rem; color: var(--primary);"></i>
            Connect With Me
        </h3>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="social-links">
            <a href="https://github.com/Aimecol" target="_blank" class="social-link">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="mailto:aimecol314@gmail.com" class="social-link">
                <i class="far fa-envelope"></i> Email Me
            </a>
            <a href="tel:+250789375245" class="social-link">
                <i class="fas fa-phone-alt"></i> Call Me
            </a>
            <a href="https://linkedin.com/" target="_blank" class="social-link">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
            <a href="https://twitter.com/" target="_blank" class="social-link">
                <i class="fab fa-twitter"></i> Twitter
            </a>
        </div>
        
        <div style="margin-top: 2rem; background: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
            <h4 style="display: flex; align-items: center; margin-bottom: 1rem; color: var(--dark);">
                <i class="fas fa-map-marked-alt" style="margin-right: 0.75rem; color: var(--primary);"></i>
                Location
            </h4>
            <p style="color: var(--dark);">Kigali, Rwanda</p>
        </div>
        ''', unsafe_allow_html=True)

elif current_menu == "Customize Profile":
    st.markdown('<div class="section-title fade-in">Customize Your Profile</div>', unsafe_allow_html=True)
    
    st.markdown("### Personal Information")
    st.session_state['name'] = st.text_input("Full Name", st.session_state['name'])
    st.session_state['location'] = st.text_input("Location", st.session_state['location'])
    st.session_state['university'] = st.text_input("University", st.session_state['university'])
    st.session_state['field'] = st.text_input("Field of Study", st.session_state['field'])
    st.session_state['bio'] = st.text_area("Bio", st.session_state['bio'])
    
    st.markdown("### Profile Picture")
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])
    if profile_pic:
        st.session_state['profile_pic'] = profile_pic
    
    st.markdown("### Resume")
    col1, col2 = st.columns([3, 1])
    
    # Check if using default resume
    is_default = False
    try:
        with open("cv.pdf", "rb") as file:
            default_content = file.read()
            if st.session_state['resume']:
                current_content = st.session_state['resume'].getvalue()
                is_default = default_content == current_content
    except:
        pass
    
    with col1:
        if is_default:
            st.info("Currently using the default resume (cv.pdf)")
            
        resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        if resume:
            st.session_state['resume'] = resume
            st.success("Resume uploaded successfully! The download button on the Home page is now functional.")
    
    with col2:
        if st.session_state['resume']:
            # Determine filename based on whether it's default or custom
            filename = "cv.pdf" if is_default else "Resume.pdf"
            
            st.markdown("""
            <div style="margin-top: 2.5rem;">
            """ + get_download_link(st.session_state['resume'], filename) + """
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Reset to Default" if not is_default else "Remove Resume"):
                if is_default:
                    st.session_state['resume'] = None
                else:
                    # Reset to default resume
                    try:
                        with open("cv.pdf", "rb") as file:
                            default_resume = BytesIO(file.read())
                            st.session_state['resume'] = default_resume
                    except:
                        st.session_state['resume'] = None
                st.rerun()
    
    st.markdown("### Skills")
    skills_to_remove = []
    for skill, level in st.session_state['skills'].items():
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            new_level = st.slider(f"{skill}", 0, 100, int(level))
            st.session_state['skills'][skill] = new_level
        with col3:
            if st.button(f"Remove {skill}"):
                skills_to_remove.append(skill)
    
    for skill in skills_to_remove:
        del st.session_state['skills'][skill]
    
    new_skill = st.text_input("Add New Skill")
    new_skill_level = st.slider("Skill Level", 0, 100, 50)
    if st.button("Add Skill") and new_skill:
        st.session_state['skills'][new_skill] = new_skill_level
        st.experimental_rerun()
    
    st.markdown("### Achievements")
    achievements_to_remove = []
    for i, achievement in enumerate(st.session_state['achievements']):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.session_state['achievements'][i] = st.text_input(f"Achievement {i+1}", achievement)
        with col2:
            if st.button(f"Remove #{i+1}"):
                achievements_to_remove.append(i)
    
    for i in sorted(achievements_to_remove, reverse=True):
        st.session_state['achievements'].pop(i)
    
    new_achievement = st.text_input("Add New Achievement")
    if st.button("Add Achievement") and new_achievement:
        st.session_state['achievements'].append(new_achievement)
        st.experimental_rerun()
    
    if st.button("Save Changes"):
        st.success("All changes saved successfully!")

st.markdown("---")
st.markdown(" 2025 | Aime Claudien Mazimpaka | Created with Streamlit")

