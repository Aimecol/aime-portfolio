# Aime Portfolio

![Portfolio Preview](https://img.shields.io/badge/Portfolio-Interactive-4361ee)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive, customizable portfolio web application built with Streamlit. This portfolio showcases professional experience, projects, skills, and achievements in a modern, responsive interface.

## 🌟 Features

- **Interactive UI**: Modern, responsive design with smooth animations and transitions
- **Customizable Content**: Easily update personal information, projects, skills, and more
- **Multiple Sections**:
  - Home with personal introduction
  - Projects showcase with filtering by category
  - Skills & Achievements with visual representation
  - Interactive Timeline of experience
  - Testimonials from colleagues and clients
  - Contact information
  - Profile customization panel
- **Resume Management**: Upload and download resume functionality with default CV
- **Dynamic Navigation**: Smooth navigation between different sections
- **Responsive Design**: Looks great on both desktop and mobile devices

## 📋 Table of Contents

- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Customization](#-customization)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 🚀 Demo

[Live Demo](https://aime-portfolio.streamlit.app/) (Coming Soon)

![Portfolio Screenshot](https://via.placeholder.com/800x400?text=Portfolio+Screenshot)

## 💻 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Aimecol/aime-portfolio.git
   cd aime-portfolio
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run portfolio.py
   ```

## 🔍 Usage

After launching the application, you'll see the portfolio with the following sections:

1. **Home**: Personal introduction and quick overview
2. **Projects**: Showcase of projects with filtering capabilities
3. **Skills & Achievements**: Visual representation of technical skills and achievements
4. **Timeline**: Chronological display of education and work experience
5. **Testimonials**: Feedback from colleagues and clients
6. **Contact**: Contact information and form
7. **Customize Profile**: Panel to update personal information, upload resume, and modify content

Navigate between sections using the sidebar navigation menu.

## ⚙️ Customization

### Personal Information

1. Click on the "Customize Profile" section in the navigation menu
2. Update your name, location, university, field of study, and bio
3. Upload a profile picture and resume
4. All changes are saved to the session state and reflected immediately

### Projects

Add or modify projects in the `projects` list in the code:

```python
projects = [
    {
        "title": "Project Title",
        "type": "Project Type",
        "year": "Year",
        "description": "Project description",
        "link": "https://project-link.com",
        "categories": ["Category1", "Category2"]
    },
    # Add more projects...
]
```

### Skills

Modify skills and proficiency levels in the session state initialization:

```python
st.session_state['skills'] = {
    "Skill Name": proficiency_percentage,
    # Add more skills...
}
```

### Timeline

Update your timeline events in the `timeline_events` list:

```python
timeline_events = [
    {
        "year": "Year",
        "event": "Event Title",
        "description": "Event description"
    },
    # Add more events...
]
```

## 📁 Project Structure

- `portfolio.py`: Main application file
- `requirements.txt`: Python dependencies
- `cv.pdf`: Default resume file
- `README.md`: Project documentation
- Static assets (images, etc.)

## 🛠️ Technologies Used

- **Streamlit**: For the web application framework
- **Python**: Core programming language
- **HTML/CSS**: For styling and layout
- **Font Awesome**: For icons
- **Base64**: For file encoding/decoding
- **BytesIO**: For file handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

Aime Claudien Mazimpaka - [GitHub](https://github.com/Aimecol)

Project Link: [https://github.com/Aimecol/aime-portfolio](https://github.com/Aimecol/aime-portfolio)

---

Made with ❤️ by Aime Claudien Mazimpaka
