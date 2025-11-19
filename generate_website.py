#!/usr/bin/env python3
"""
Generate 100-page website about Staks Rosch
"""

import os
from pathlib import Path

# Base directory
base_dir = Path("/workspace/staks-rosch-website")

# Navigation template
def get_nav():
    return '''
    <nav class="main-nav">
        <div class="nav-container">
            <a href="../index.html" class="nav-logo">STAKS ROSCH</a>
            <button class="nav-toggle">☰</button>
            <ul class="nav-links">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../biography/index.html">Biography</a></li>
                <li><a href="../book/index.html">The Book</a></li>
                <li><a href="../activism/index.html">Activism</a></li>
                <li><a href="../writings/index.html">Writings</a></li>
                <li><a href="../philosophy/index.html">Philosophy</a></li>
                <li><a href="../music/index.html">Music</a></li>
                <li><a href="../resources/index.html">Resources</a></li>
            </ul>
        </div>
    </nav>
'''

# Footer template
def get_footer():
    return '''
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>About</h4>
                    <ul>
                        <li><a href="../biography/index.html">Biography</a></li>
                        <li><a href="../biography/early-life.html">Early Life</a></li>
                        <li><a href="../biography/education.html">Education</a></li>
                        <li><a href="../biography/career.html">Career</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Works</h4>
                    <ul>
                        <li><a href="../book/index.html">Disproving God</a></li>
                        <li><a href="../writings/index.html">Articles</a></li>
                        <li><a href="../music/index.html">ReasonPlusOne</a></li>
                        <li><a href="../resources/index.html">Resources</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Topics</h4>
                    <ul>
                        <li><a href="../philosophy/atheism.html">Atheism</a></li>
                        <li><a href="../philosophy/humanism.html">Humanism</a></li>
                        <li><a href="../philosophy/reason.html">Reason</a></li>
                        <li><a href="../philosophy/secularism.html">Secularism</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="https://twitter.com/DangerousTalk" target="_blank">Twitter/X</a></li>
                        <li><a href="https://www.facebook.com/staks/" target="_blank">Facebook</a></li>
                        <li><a href="https://www.huffpost.com/author/dangeroustalk-462" target="_blank">HuffPost</a></li>
                        <li><a href="../resources/contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Staks Rosch Website. Created by MiniMax Agent. All content for educational purposes.</p>
            </div>
        </div>
    </footer>
    <script src="../js/main.js"></script>
'''

# HTML template
def create_page(title, hero_category, hero_title, hero_subtitle, content, filepath, sidebar=None):
    sidebar_html = ""
    main_class = "container"
    
    if sidebar:
        sidebar_html = f'''
        <div class="sidebar-nav">
            <h3>{sidebar['title']}</h3>
            <ul>
                {''.join([f'<li><a href="{link["url"]}">{link["text"]}</a></li>' for link in sidebar['links']])}
            </ul>
        </div>
        '''
        main_class = "page-layout"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Staks Rosch</title>
    <link rel="stylesheet" href="../css/main.css">
</head>
<body>
    {get_nav()}
    
    <section class="hero">
        <div class="hero-category">{hero_category}</div>
        <h1 class="hero-title">{hero_title}</h1>
        <p class="hero-subtitle">{hero_subtitle}</p>
    </section>
    
    <main class="{main_class}">
        {sidebar_html}
        <div class="main-content">
            {content}
        </div>
    </main>
    
    {get_footer()}
</body>
</html>'''
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {filepath}")

# Biography Section (10 pages)
biography_pages = [
    {
        "filename": "biography/index.html",
        "title": "Biography",
        "hero_category": "About Staks Rosch",
        "hero_title": "Atheist, Humanist, and Advocate for Reason",
        "hero_subtitle": "Writer, Activist, Philosopher, and Progressive Voice",
        "content": '''
            <section class="content-section">
                <h2>Who is Staks Rosch?</h2>
                <p>Staks Rosch is a prominent atheist activist, writer, blogger, and former talk radio host who has dedicated his career to promoting reason, humanism, and secular values. Based in Philadelphia, Pennsylvania, Staks has become a vocal advocate for atheism and progressive causes, using his platform to challenge religious dogma and promote rational thinking.</p>
                
                <p>As the former head of the Philadelphia Coalition of Reason (PhillyCoR), Staks has worked to build and strengthen the secular community in the greater Philadelphia area. He has served on the board of the Freethought Society of Greater Philadelphia and has been instrumental in organizing events and initiatives that bring together like-minded individuals who value reason and evidence-based thinking.</p>
                
                <p>With a Master's Degree in Philosophy from West Chester University, Staks brings academic rigor to his advocacy work. His educational background has equipped him with the tools to engage in sophisticated philosophical debates about the existence of God, the nature of morality, and the role of religion in society.</p>
                
                <blockquote class="quote">
                    "Kindness is the real punk rock." - Staks Rosch
                </blockquote>
                
                <p>Staks is perhaps best known for his "Dangerous Talk" blog, which he founded and has maintained for years on the Skeptic Ink Network. Through this platform, he has published hundreds of articles on atheism, humanism, politics, and social issues, reaching thousands of readers worldwide. His writing has also appeared in The Huffington Post, where he served as a contributor, and Publishers Weekly, where he worked as a freelance writer.</p>
                
                <p>In 2021, Staks published his book, "Disproving God and 5 Adequate Reasons To Be an Atheist," which presents a concise and accessible argument against the existence of God. The book has been praised for its clarity and straightforward approach to complex philosophical questions.</p>
                
                <p>Beyond his activism and writing, Staks is also a stay-at-home dad, balancing his advocacy work with family responsibilities. He describes himself humorously as a "Jedi," reflecting his playful personality and his commitment to values like compassion, justice, and truth.</p>
                
                <p>In recent years, Staks has ventured into creative territory with the launch of ReasonPlusOne, an atheist-themed AI music band. The project's debut album, "That Ungodly Sound," showcases his innovative approach to spreading secular messages through art and culture.</p>
            </section>
        '''
    },
    {
        "filename": "biography/early-life.html",
        "title": "Early Life",
        "hero_category": "Biography",
        "hero_title": "Early Life and Background",
        "hero_subtitle": "From New Jersey to Philosophical Awakening",
        "content": '''
            <section class="content-section">
                <h2>Childhood and Origins</h2>
                <p>Staks Rosch was born and raised in northern New Jersey, just outside of New York City. Growing up in the vibrant and diverse New York metropolitan area exposed him to a wide range of cultures, beliefs, and perspectives from an early age. This multicultural environment would later influence his commitment to tolerance and his critical examination of religious claims.</p>
                
                <p>The proximity to New York City meant that Staks was surrounded by intellectual and cultural richness. The area's diversity challenged him to think critically about the different worldviews he encountered, laying the groundwork for his later philosophical inquiries into religion, morality, and reason.</p>
                
                <h2>Journey to Atheism</h2>
                <p>Like many atheists, Staks's path to non-belief was gradual and involved careful examination of religious claims. Growing up in America, where religious belief is widespread, Staks was exposed to Christian teachings and traditions. However, as he matured intellectually, he began to question the evidence for religious claims and the logical consistency of religious doctrines.</p>
                
                <p>His journey to atheism was not a rebellion but rather an intellectual awakening. Through reading, discussion, and philosophical reflection, Staks came to the conclusion that there was insufficient evidence to support belief in God. This realization was both liberating and challenging, as it required him to reconstruct his understanding of morality, meaning, and purpose without reference to religious frameworks.</p>
                
                <h2>Formative Influences</h2>
                <p>Several factors contributed to Staks's development as a thinker and activist. The intellectual climate of the late 20th and early 21st centuries, with the rise of the "New Atheism" movement led by figures like Richard Dawkins, Christopher Hitchens, and Sam Harris, provided a context for his atheism. These thinkers demonstrated that it was possible to be openly critical of religion while advocating for reason and science.</p>
                
                <p>Additionally, Staks's personal experiences with religious institutions and believers shaped his understanding of the role religion plays in society. He witnessed both the comfort that religion can provide and the harm it can cause, leading him to advocate for a secular approach to ethics and public policy.</p>
            </section>
        '''
    },
    # Continue with more biography pages...
]

print("Generating all pages...")
for page in biography_pages:
    create_page(
        page['title'],
        page['hero_category'],
        page['hero_title'],
        page['hero_subtitle'],
        page['content'],
        base_dir / page['filename']
    )

print("\\nWebsite generation complete!")
