#!/usr/bin/env python3
"""
Update key pages with detailed information from the pasted content
"""

import os
from pathlib import Path

base_dir = Path("/workspace/staks-rosch-website")

# Activism page with I-95 billboard and detailed PhillyCoR info
activism_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activism - Staks Rosch</title>
    <link rel="stylesheet" href="../css/main.css">
</head>
<body>
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
    
    <section class="hero">
        <div class="hero-category">Activism</div>
        <h1 class="hero-title">Secular Activism & Community Building</h1>
        <p class="hero-subtitle">Building the Freethought Movement</p>
    </section>
    
    <main class="container">
        <div class="main-content content-column">
            
        <section class="section">
            <h2>Activism at the Core</h2>
            <p>Activism is at the core of Staks Rosch's career. He has been heavily involved in organizing the secular community, particularly in the Philadelphia area. His approach to activism is consistently non-violent and education-focused. As he writes, "what atheists like me advocate is not eliminating religion [by force], but rather eliminating the influence of religion through education."</p>
            
            <h2>Philadelphia Coalition of Reason (PhillyCoR)</h2>
            <p>Rosch served as the head of the <strong>Philadelphia Coalition of Reason (PhillyCoR)</strong>, an umbrella organization uniting local atheist, humanist, skeptic, and freethought groups. In this leadership role, he coordinated events and outreach to bring nonbelievers together and into the public square.</p>
            
            <h3>The I-95 Billboard Campaign</h3>
            <p>PhillyCoR garnered national attention for campaigns like a prominent billboard on <strong>Interstate 95 reading "Don't believe in God? You are not alone."</strong> This was an invitation for questioning believers and nonreligious people to connect with the secular community, demonstrating that atheists and humanists are present and welcoming in Philadelphia.</p>
            
            <p>Under Rosch's coordination, PhillyCoR and its member groups hosted educational meetings, social gatherings, and media campaigns to raise the visibility of non-theists and defend the separation of church and state.</p>
            
            <h2>Freethought Society of Greater Philadelphia</h2>
            <p>Beyond PhillyCoR, Rosch was a board member of the <strong>Freethought Society of Greater Philadelphia</strong>, working alongside other activists to support church-state separation and scientific thinking in the region. His board service helped strengthen one of the area's most important secular organizations.</p>
            
            <h2>Political Engagement</h2>
            <p>Rosch has also personally engaged in political activism. He notes that he once traveled to Washington, D.C. to lobby U.S. Senators in favor of free speech protections. A self-described progressive, he has been active in Democratic Party circles while maintaining an independent critical outlook.</p>
            
            <p>Rosch's activism encompasses civil rights advocacy, championing equality for women, LGBTQ individuals, and religious minorities, as well as public policy work on issues from education to freedom of expression.</p>
            
            <h2>Media & Cultural Activism</h2>
            <p>Importantly, Rosch's activism often bridges into media and culture. He hosted <strong>"Dangerous Talk"</strong> as an atheist radio show on <strong>WCHE 1520 AM</strong> in Pennsylvania, using the airwaves to discuss atheism, politics, and social issues with a broad audience. He humorously dubbed religion, politics, and sex as "the three most dangerous topics of polite conversation."</p>
            
            <p>The radio show later moved online to the <strong>Freethought Radio Podcast Network</strong>—airing alongside programs like The Infidel Guy and The Rational Response Squad—extending its reach to an internet audience. Through these platforms, Rosch gave voice to atheist perspectives and built a community of "Dangerous Talkers."</p>
            
            <h2>Philosophy of Activism</h2>
            <blockquote class="quote">
                "What atheists like me advocate is not eliminating religion, but rather eliminating the influence of religion through education."
            </blockquote>
            
            <p>By organizing coalitions, creating content, and directly engaging with both lawmakers and the public, Staks Rosch has been a tireless advocate for secularism and humanist values. His work demonstrates that effective activism requires both principled commitment and practical organizing skills.</p>
        </section>
    
        </div>
    </main>
    
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>About</h4>
                    <ul>
                        <li><a href="../biography/index.html">Biography</a></li>
                        <li><a href="../book/index.html">The Book</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Works</h4>
                    <ul>
                        <li><a href="../writings/index.html">Articles</a></li>
                        <li><a href="../music/index.html">Music</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Topics</h4>
                    <ul>
                        <li><a href="../philosophy/atheism.html">Atheism</a></li>
                        <li><a href="../philosophy/humanism.html">Humanism</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="https://twitter.com/DangerousTalk" target="_blank">Twitter/X</a></li>
                        <li><a href="https://www.facebook.com/staks/" target="_blank">Facebook</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Staks Rosch Website. All content for educational purposes.</p>
            </div>
        </div>
    </footer>
    <script src="../js/main.js"></script>
</body>
</html>'''

# Read then write activism page
with open(base_dir / "activism/index.html", 'r') as f:
    pass

with open(base_dir / "activism/index.html", 'w') as f:
    f.write(activism_content)

print("✓ Updated activism/index.html")

# Writings page with Dangerous Talk details, HuffPost, Publishers Weekly
writings_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Writings - Staks Rosch</title>
    <link rel="stylesheet" href="../css/main.css">
</head>
<body>
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
    
    <section class="hero">
        <div class="hero-category">Writings</div>
        <h1 class="hero-title">Articles, Essays & Blog Posts</h1>
        <p class="hero-subtitle">Comprehensive Archive of Written Work</p>
    </section>
    
    <main class="container">
        <div class="main-content content-column">
            
        <section class="section">
            <h2>Extensive Portfolio</h2>
            <p>Staks Rosch has an extensive portfolio of writings that advance atheist and humanist ideas. His articles combine humor with pointed critiques of religious doctrine and advocacy of skepticism, reaching thousands of readers across multiple platforms.</p>
            
            <h2>Dangerous Talk Blog</h2>
            <p>He first gained renown through his blog <strong>Dangerous Talk</strong>, which began as a college radio show and evolved into a daily blog by 2006. On DangerousTalk.net, Rosch published regular commentary on "the three most dangerous topics"—religion, politics, and sex—from a secular progressive standpoint.</p>
            
            <p>His blog posts often combined humor with pointed critiques of religious doctrine. For example, he dissected concepts like faith healing with satirical articles such as "The Bible Cured Cancer!" In 2013, Rosch brought Dangerous Talk into the <strong>Skeptic Ink Network</strong> (a collective of secular bloggers), where he continues to write analytical pieces on current events and atheist thought.</p>
            
            <h3>Popular Blog Series</h3>
            <ul>
                <li><strong>Atheism 101</strong> - Basic answers to questions about atheism</li>
                <li><strong>Question Quesday</strong> - Playfully addressing quirky theological questions</li>
                <li><strong>Ask an Atheist</strong> - Advice column format</li>
            </ul>
            
            <h2>National Atheism Examiner</h2>
            <p>In addition to blogging, Rosch served as the <strong>National Atheism Examiner on Examiner.com</strong>, writing articles to inform and unite the atheist community. This platform allowed him to reach a broader audience with news and commentary relevant to secular Americans.</p>
            
            <h2>The Huffington Post</h2>
            <p>As a <strong>Huffington Post contributor</strong>, Rosch reached a wider audience with op-eds and informational pieces on secularism. His HuffPost articles included topics such as biblical criticism—e.g., explaining why "The Biblical Exodus Story Is Fiction"—as well as political commentary from an atheist viewpoint.</p>
            
            <p>Rosch's writing is known for being direct yet accessible; he often writes in a conversational tone to invite those unfamiliar with atheism into the discussion.</p>
            
            <h2>Publishers Weekly</h2>
            <p>Notably, Staks Rosch is also a <strong>freelance writer for Publishers Weekly</strong>, focusing on religion and spirituality books. In this role, he conducts interviews with authors across the belief spectrum.</p>
            
            <blockquote class="quote">
                "Being a freelance writer for Publishers Weekly gives me the opportunity to interview atheist and humanist authors and help put their books into the marketplace of ideas."
            </blockquote>
            
            <p>He has profiled prominent voices such as scientists examining belief, ex-clergy turned atheist writers, and religious authors grappling with secularism. Examples include interviews about books like <em>The Phantom God</em> by John C. Wathey and <em>Hi, I'm an Atheist!</em> by David G. McAfee.</p>
            
            <p>Through these Q&A pieces, Rosch facilitates dialogue on faith and doubt in a respectful, journalistic manner. His Publishers Weekly interviews bridge worlds—introducing humanist ideas to religious readers and vice versa—which he views as an extension of his activism to normalize atheism in mainstream culture.</p>
            
            <h2>Writing Style & Impact</h2>
            <p>Across all these writing platforms, Rosch's content consistently promotes reason, skepticism, and humanist ethics. Whether blogging passionately on Dangerous Talk or writing for national publications, he uses the written word to challenge dogma and encourage evidence-based thinking.</p>
            
            <p>His versatility as a writer—spanning personal blogs, news outlets, and literary journalism—has made Staks Rosch a familiar name in secular circles. His articles have reached thousands of readers, offering both a rational critique of religion and a positive case for humanist values in society.</p>
        </section>
    
        </div>
    </main>
    
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>About</h4>
                    <ul>
                        <li><a href="../biography/index.html">Biography</a></li>
                        <li><a href="../book/index.html">The Book</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Works</h4>
                    <ul>
                        <li><a href="../writings/index.html">Articles</a></li>
                        <li><a href="../music/index.html">Music</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Topics</h4>
                    <ul>
                        <li><a href="../philosophy/atheism.html">Atheism</a></li>
                        <li><a href="../philosophy/humanism.html">Humanism</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="https://twitter.com/DangerousTalk" target="_blank">Twitter/X</a></li>
                        <li><a href="https://www.facebook.com/staks/" target="_blank">Facebook</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Staks Rosch Website. All content for educational purposes.</p>
            </div>
        </div>
    </footer>
    <script src="../js/main.js"></script>
</body>
</html>'''

# Read then write writings page
with open(base_dir / "writings/index.html", 'r') as f:
    pass

with open(base_dir / "writings/index.html", 'w') as f:
    f.write(writings_content)

print("✓ Updated writings/index.html")

print("\n✓ All major pages updated with detailed information!")
print("✓ Enhanced content includes:")
print("  - Jewish background and de-conversion story")
print("  - I-95 billboard campaign details")
print("  - Reason+1 music project with song titles")
print("  - Publishers Weekly interview work")
print("  - Dangerous Talk blog history")
print("  - Book pricing and critical acclaim")
