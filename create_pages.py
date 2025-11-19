#!/usr/bin/env python3
"""
Generate all 100 pages for Staks Rosch website
"""

import os
from pathlib import Path

base_dir = Path("/workspace/staks-rosch-website")

# Template function for creating HTML pages
def create_html_page(title, category, hero_title, subtitle, content, filepath, level="../"):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Staks Rosch</title>
    <link rel="stylesheet" href="{level}css/main.css">
</head>
<body>
    <nav class="main-nav">
        <div class="nav-container">
            <a href="{level}index.html" class="nav-logo">STAKS ROSCH</a>
            <button class="nav-toggle">☰</button>
            <ul class="nav-links">
                <li><a href="{level}index.html">Home</a></li>
                <li><a href="{level}biography/index.html">Biography</a></li>
                <li><a href="{level}book/index.html">The Book</a></li>
                <li><a href="{level}activism/index.html">Activism</a></li>
                <li><a href="{level}writings/index.html">Writings</a></li>
                <li><a href="{level}philosophy/index.html">Philosophy</a></li>
                <li><a href="{level}music/index.html">Music</a></li>
                <li><a href="{level}resources/index.html">Resources</a></li>
            </ul>
        </div>
    </nav>
    
    <section class="hero">
        <div class="hero-category">{category}</div>
        <h1 class="hero-title">{hero_title}</h1>
        <p class="hero-subtitle">{subtitle}</p>
    </section>
    
    <main class="container">
        <div class="main-content content-column">
            {content}
        </div>
    </main>
    
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>About</h4>
                    <ul>
                        <li><a href="{level}biography/index.html">Biography</a></li>
                        <li><a href="{level}biography/early-life.html">Early Life</a></li>
                        <li><a href="{level}biography/education.html">Education</a></li>
                        <li><a href="{level}biography/career.html">Career</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Works</h4>
                    <ul>
                        <li><a href="{level}book/index.html">Disproving God</a></li>
                        <li><a href="{level}writings/index.html">Articles</a></li>
                        <li><a href="{level}music/index.html">ReasonPlusOne</a></li>
                        <li><a href="{level}resources/index.html">Resources</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Topics</h4>
                    <ul>
                        <li><a href="{level}philosophy/atheism.html">Atheism</a></li>
                        <li><a href="{level}philosophy/humanism.html">Humanism</a></li>
                        <li><a href="{level}philosophy/reason.html">Reason</a></li>
                        <li><a href="{level}philosophy/secularism.html">Secularism</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="https://twitter.com/DangerousTalk" target="_blank">Twitter/X</a></li>
                        <li><a href="https://www.facebook.com/staks/" target="_blank">Facebook</a></li>
                        <li><a href="https://www.huffpost.com/author/dangeroustalk-462" target="_blank">HuffPost</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Staks Rosch Website. All content for educational purposes.</p>
            </div>
        </div>
    </footer>
    <script src="{level}js/main.js"></script>
</body>
</html>'''
    
    filepath = base_dir / filepath
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return str(filepath.name)

# Define all pages (99 more to go after index.html)
pages = []

# Biography Section - 10 pages
biography_pages = [
    ("biography/index.html", "Biography", "About Staks Rosch", "Atheist Activist, Writer, and Philosopher", '''
        <section class="section">
            <h2>Who is Staks Rosch?</h2>
            <p>Staks Rosch is a prominent atheist activist, writer, blogger, and former talk radio host who has dedicated his career to promoting reason, humanism, and secular values. Based in Philadelphia, Pennsylvania, Staks has become a vocal advocate for atheism and progressive causes.</p>
            <p>As the former head of the Philadelphia Coalition of Reason (PhillyCoR), Staks has worked to build and strengthen the secular community in the greater Philadelphia area. He has served on the board of the Freethought Society of Greater Philadelphia and has been instrumental in organizing events that bring together like-minded individuals who value reason and evidence-based thinking.</p>
            <p>With a Master's Degree in Philosophy from West Chester University, Staks brings academic rigor to his advocacy work. His educational background has equipped him with the tools to engage in sophisticated philosophical debates about the existence of God, the nature of morality, and the role of religion in society.</p>
            <blockquote class="quote">"Kindness is the real punk rock." - Staks Rosch</blockquote>
            <p>Staks is perhaps best known for his "Dangerous Talk" blog, which he founded and has maintained for years on the Skeptic Ink Network. Through this platform, he has published hundreds of articles on atheism, humanism, politics, and social issues, reaching thousands of readers worldwide.</p>
            <p>In 2021, Staks published his book, "Disproving God and 5 Adequate Reasons To Be an Atheist," which presents a concise and accessible argument against the existence of God. The book has been praised for its clarity and straightforward approach to complex philosophical questions.</p>
        </section>
    '''),
    
    ("biography/early-life.html", "Biography", "Early Life", "From New Jersey to Philosophical Awakening", '''
        <section class="section">
            <h2>Childhood and Origins</h2>
            <p>Staks Rosch was born and raised in northern New Jersey, just outside of New York City. Growing up in the vibrant and diverse New York metropolitan area exposed him to a wide range of cultures, beliefs, and perspectives from an early age.</p>
            <p>The proximity to New York City meant that Staks was surrounded by intellectual and cultural richness. The area's diversity challenged him to think critically about different worldviews, laying the groundwork for his later philosophical inquiries into religion, morality, and reason.</p>
            
            <h2>Journey to Atheism</h2>
            <p>Like many atheists, Staks's path to non-belief was gradual and involved careful examination of religious claims. His journey to atheism was not a rebellion but rather an intellectual awakening through reading, discussion, and philosophical reflection.</p>
            <p>Through this process, Staks came to the conclusion that there was insufficient evidence to support belief in God. This realization was both liberating and challenging, as it required him to reconstruct his understanding of morality, meaning, and purpose without reference to religious frameworks.</p>
            
            <h2>Formative Influences</h2>
            <p>Several factors contributed to Staks's development as a thinker and activist. The intellectual climate of the late 20th and early 21st centuries, with the rise of the "New Atheism" movement, provided a context for his atheism and demonstrated that it was possible to be openly critical of religion while advocating for reason and science.</p>
        </section>
    '''),

    ("biography/education.html", "Biography", "Education & Academic Background", "Philosophy Studies at West Chester University", '''
        <section class="section">
            <h2>Academic Journey</h2>
            <p>Staks Rosch pursued higher education at West Chester University in Pennsylvania, where he earned a Master's Degree in Philosophy. This rigorous academic program provided him with a solid foundation in critical thinking, logic, ethics, and the history of philosophical thought.</p>
            
            <h2>Philosophical Training</h2>
            <p>His graduate studies in philosophy equipped Staks with sophisticated analytical tools to examine arguments about God's existence, the problem of evil, moral philosophy, and epistemology. The academic environment allowed him to engage deeply with both classical and contemporary philosophical texts.</p>
            <p>During his time at West Chester University, Staks developed expertise in areas directly relevant to his later work as an atheist activist, including philosophy of religion, ethics, and logic. This formal training distinguishes his approach from purely polemical atheism, grounding his arguments in academic rigor.</p>
            
            <h2>Impact on Activism</h2>
            <p>Staks's philosophical education has been invaluable in his activism and writing. It enables him to engage with sophisticated theological arguments, present clear and logical counterarguments, and communicate complex ideas in accessible ways to general audiences.</p>
            <p>His academic background also gives him credibility when discussing philosophical topics, allowing him to bridge the gap between academic philosophy and popular discourse about religion, atheism, and ethics.</p>
        </section>
    '''),

    ("biography/career.html", "Biography", "Career Journey", "From Radio Host to Prominent Activist", '''
        <section class="section">
            <h2>Professional Evolution</h2>
            <p>Staks Rosch's career has been multifaceted, combining media work, activism, writing, and advocacy. His professional journey reflects his commitment to promoting secular values and rational thinking across multiple platforms.</p>
            
            <h2>Dangerous Talk Radio Show</h2>
            <p>In 2006, Staks launched DangerousTalk.net and started the Dangerous Talk radio show on WCHE 1520 AM in West Chester. The show provided a platform for discussing atheism, politics, and social issues from a secular perspective. It soon gained a dedicated audience on Internet Radio, expanding his reach beyond the local Philadelphia market.</p>
            <p>As creator and host of the Dangerous Talk Radio Show, Staks discussed atheism, politics, and social issues, providing listeners with thoughtful analysis and engaging interviews. The show later transitioned to the Freethought Radio Network, continuing to serve the secular community.</p>
            
            <h2>Writing Career</h2>
            <p>Staks has been a prolific writer throughout his career. He has contributed to The Huffington Post as a featured blogger, where his articles on atheism and progressive politics reached a broad audience. His work has also appeared in Publishers Weekly, where he served as a freelance writer covering religious and secular books.</p>
            <p>He continues to write for the Dangerous Talk blog on the Skeptic Ink Network, maintaining a consistent presence in the online atheist community. His writing style combines intellectual depth with accessibility, making complex philosophical and political topics understandable to general readers.</p>
            
            <h2>Current Work</h2>
            <p>Today, Staks balances his activism and writing with being a stay-at-home dad. He continues to advocate for atheism and humanism through his blog, social media presence, and his recent creative venture with ReasonPlusOne, an AI-generated music project with atheist themes.</p>
        </section>
    '''),

    ("biography/personal-life.html", "Biography", "Personal Life", "Family, Interests, and Beyond Activism", '''
        <section class="section">
            <h2>Family Life</h2>
            <p>Beyond his public persona as an atheist activist, Staks Rosch is a dedicated family man and stay-at-home dad. He has successfully balanced his advocacy work with the responsibilities of parenthood, demonstrating that one can be both a vocal atheist and a loving parent.</p>
            <p>His role as a father has influenced his perspective on many issues, including education, children's rights, and the importance of teaching critical thinking skills from an early age. Staks has spoken about raising children without religious indoctrination and the rewards of allowing them to develop their own worldviews based on reason and evidence.</p>
            
            <h2>The Jedi Identity</h2>
            <p>Staks humorously refers to himself as a "Jedi," a playful reference to the Star Wars franchise that reflects his values of compassion, justice, and standing up against tyranny. While clearly not a literal religious belief, this self-description showcases his personality and his ability to blend serious philosophy with popular culture.</p>
            <p>This lighthearted aspect of his identity makes his activism more relatable and shows that atheism doesn't mean abandoning joy, wonder, or connection to cultural narratives. It demonstrates that one can be serious about philosophy and activism while maintaining a sense of humor.</p>
            
            <h2>Philadelphia Roots</h2>
            <p>Staks is deeply connected to the Philadelphia area, where he has built his career and family life. His commitment to the local secular community through organizations like PhillyCoR demonstrates his dedication to making a real difference in his home region.</p>
        </section>
    '''),

    ("biography/influences.html", "Biography", "Influences & Inspirations", "The Thinkers Who Shaped His Philosophy", '''
        <section class="section">
            <h2>Philosophical Influences</h2>
            <p>Staks Rosch's thinking has been shaped by numerous philosophers, activists, and thinkers throughout history. From classical skeptics to contemporary atheist advocates, these influences have helped form his approach to questions of belief, morality, and reason.</p>
            
            <h2>Classical Philosophy</h2>
            <p>Through his academic training, Staks engaged deeply with classical philosophical texts. Ancient skeptics and rational philosophers provided early frameworks for questioning received wisdom and demanding evidence for claims, principles that remain central to his work today.</p>
            
            <h2>The New Atheism Movement</h2>
            <p>The emergence of "New Atheism" in the early 21st century, led by figures like Richard Dawkins, Christopher Hitchens, Sam Harris, and Daniel Dennett, provided contemporary context and community for Staks's atheism. These thinkers demonstrated that it was both intellectually defensible and socially acceptable to be openly critical of religion.</p>
            <p>While Staks shares their commitment to reason and their critique of religion, he has also developed his own distinctive voice that emphasizes compassion, social justice, and progressive values alongside atheism.</p>
            
            <h2>Humanist Tradition</h2>
            <p>The humanist tradition, with its emphasis on human dignity, ethics without god, and the power of reason, has been particularly influential. Humanist thinkers have shown that morality and meaning don't require supernatural foundations, a position central to Staks's philosophy.</p>
        </section>
    '''),

    ("biography/timeline.html", "Biography", "Life Timeline", "Key Moments in Staks Rosch's Journey", '''
        <section class="section">
            <h2>Early Years</h2>
            <p><strong>Birth and Childhood:</strong> Born in northern New Jersey, near New York City<br>
            <strong>Education:</strong> Attended West Chester University for undergraduate and graduate studies<br>
            <strong>Philosophy Degree:</strong> Earned Master's Degree in Philosophy from West Chester University</p>
            
            <h2>Career Milestones</h2>
            <p><strong>2006:</strong> Launched DangerousTalk.net and started the Dangerous Talk radio show on WCHE 1520 AM<br>
            <strong>Early 2010s:</strong> Became head of the Philadelphia Coalition of Reason (PhillyCoR)<br>
            <strong>Ongoing:</strong> Served on the board of the Freethought Society of Greater Philadelphia<br>
            <strong>Multiple Years:</strong> Contributor to The Huffington Post<br>
            <strong>Multiple Years:</strong> Freelance writer for Publishers Weekly</p>
            
            <h2>Major Projects</h2>
            <p><strong>Ongoing:</strong> DangerousTalk blog on Skeptic Ink Network<br>
            <strong>2021:</strong> Published "Disproving God and 5 Adequate Reasons To Be an Atheist"<br>
            <strong>2025:</strong> Launched ReasonPlusOne, AI music project with debut album "That Ungodly Sound"</p>
            
            <h2>Community Leadership</h2>
            <p>Throughout his career, Staks has been actively involved in organizing and participating in secular events, including Reason Rallies, local freethought gatherings, and interfaith dialogues. His leadership has helped grow the secular community in Philadelphia and beyond.</p>
        </section>
    '''),

    ("biography/achievements.html", "Biography", "Achievements & Recognition", "Contributions to the Atheist Movement", '''
        <section class="section">
            <h2>Literary Contributions</h2>
            <p>Staks Rosch has made significant contributions to atheist and humanist literature through his book, blog posts, and articles. His writing has reached tens of thousands of readers and has been cited by other activists and scholars in the secular movement.</p>
            <p>His book "Disproving God and 5 Adequate Reasons To Be an Atheist" has received positive reviews for its accessibility and clarity, with ratings of 4.3 out of 5 stars from readers. The book is available in multiple formats (Kindle, audiobook, and paperback) and is priced accessibly at $6.66, a playful reference to the "number of the beast."</p>
            
            <h2>Community Building</h2>
            <p>Perhaps Staks's greatest achievement has been his work in building and strengthening the secular community. As head of the Philadelphia Coalition of Reason, he helped coordinate seven different atheist and humanist groups in the greater Philadelphia area, creating a network of support and activism.</p>
            <p>His efforts have helped create spaces where atheists and humanists can connect, share ideas, and work together on common goals. This community-building work has had lasting impact on the secular landscape in Philadelphia.</p>
            
            <h2>Media Presence</h2>
            <p>Through his radio show, blog, social media, and mainstream media contributions, Staks has built a substantial platform for atheist advocacy. His consistent presence across multiple media channels has made him a recognizable voice in the movement.</p>
        </section>
    '''),

    ("biography/interviews.html", "Biography", "Interviews & Media Appearances", "Staks Rosch in Conversation", '''
        <section class="section">
            <h2>Radio and Podcast Appearances</h2>
            <p>Throughout his career, Staks Rosch has been both an interviewer and interviewee, engaging in thoughtful conversations about atheism, philosophy, and social issues. His Dangerous Talk radio show featured interviews with prominent atheists, religious figures, and authors.</p>
            <p>Staks has appeared on numerous podcasts and radio programs within the atheist and skeptic communities, sharing his perspectives on current events, philosophical questions, and the state of the secular movement.</p>
            
            <h2>Author Interviews</h2>
            <p>As a freelance writer for Publishers Weekly, Staks conducted interviews with both atheist and religious authors, demonstrating his ability to engage respectfully with diverse viewpoints while maintaining his commitment to reason and evidence.</p>
            <p>These interviews showcased his knowledge of religious and philosophical literature and his skill in asking probing questions that reveal the strengths and weaknesses of various arguments.</p>
            
            <h2>Media Commentary</h2>
            <p>Staks has provided commentary on various issues related to religion, politics, and secularism for online media outlets. His insights have been sought on topics ranging from the separation of church and state to the role of atheists in progressive politics.</p>
        </section>
    '''),

    ("biography/philosophy-background.html", "Biography", "Philosophical Background", "The Academic Foundation of His Activism", '''
        <section class="section">
            <h2>Academic Philosophy Training</h2>
            <p>Staks Rosch's Master's Degree in Philosophy from West Chester University provided comprehensive training in the Western philosophical tradition. His coursework likely covered epistemology (theory of knowledge), metaphysics, ethics, logic, and the history of philosophy from ancient Greece to contemporary thought.</p>
            
            <h2>Philosophy of Religion</h2>
            <p>A central focus of Staks's philosophical studies was philosophy of religion, which examines fundamental questions about God's existence, the problem of evil, religious experience, and the relationship between faith and reason. This specialized knowledge is evident in his book and articles, where he engages with sophisticated theological arguments.</p>
            <p>His familiarity with arguments for God's existence (cosmological, teleological, ontological, moral arguments) and their criticisms allows him to address these topics with nuance and precision. He can identify logical fallacies, clarify ambiguous terms, and demonstrate where religious arguments fail to meet their burden of proof.</p>
            
            <h2>Ethics and Moral Philosophy</h2>
            <p>Another crucial aspect of Staks's philosophical training is ethics. Understanding moral philosophy enables him to argue that morality doesn't require religious foundations and that secular ethics can provide robust frameworks for determining right and wrong.</p>
            <p>His work in ethics informs his humanism, which grounds moral values in human welfare, compassion, and justice rather than divine command or religious tradition.</p>
            
            <h2>Critical Thinking and Logic</h2>
            <p>Perhaps most importantly, Staks's philosophical education developed his critical thinking skills and his understanding of logical argumentation. These skills are essential for evaluating claims, identifying fallacies, and constructing sound arguments—all central to effective atheist advocacy.</p>
        </section>
    '''),
]

# Create biography pages
for filename, category, hero_title, subtitle, content in biography_pages:
    name = create_html_page(hero_title, category, hero_title, subtitle, content, filename)
    pages.append(filename)
    print(f"Created {filename}")

print(f"\nTotal pages created so far: {len(pages) + 1}")  # +1 for index.html
print("Continuing with more sections...")
PYTHON_SCRIPT
