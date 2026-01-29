% MTecknology's Resume
%%%%
% Author: Michael Lustfield
% License: CC-BY-4
% - https://creativecommons.org/licenses/by/4.0/legalcode.txt
%%%%

\documentclass[letterpaper,10pt]{article}

%%%%%%%%%%%%%%%%%%%%%%%
%% BEGIN_FILE: mteck.sty
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{fontawesome5}
\usepackage{multicol}
\usepackage{bookmark}
\usepackage{lastpage}
\usepackage{CormorantGaramond}
\usepackage{charter}
\usepackage{xcolor}

\definecolor{accentTitle}{HTML}{000000}
\definecolor{accentText}{HTML}{000000}
\definecolor{accentLine}{HTML}{000000}

\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\urlstyle{same}

\addtolength{\oddsidemargin}{-0.7in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-0.7in}
\addtolength{\textheight}{1.4in}

\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
\setlength{\tabcolsep}{0pt}
\setlength{\footskip}{3.7pt}
\raggedbottom
\raggedright

\input{glyphtounicode}
\pdfgentounicode=1

% Custom Commands

\newcommand{\documentTitle}[2]{
 \begin{center}
  {\Huge\color{accentTitle} #1}
  \vspace{10pt}
  {\color{accentLine} \hrule}
  \vspace{2pt}
  \footnotesize{#2}
  \vspace{2pt}
  {\color{accentLine} \hrule}
 \end{center}
}

\newcommand{\documentFooter}[1]{
 \setlength{\footskip}{10.25pt}
 \fancyfoot[C]{\footnotesize #1}
}

\newcommand{\numberedPages}{
 \documentFooter{\thepage/\pageref{LastPage}}
}

\titleformat{\section}{
 \vspace{-5pt}
 \color{accentText}
 \raggedright\large\bfseries
}{}{0em}{}[\color{accentLine}\titlerule]

\newcommand{\tinysection}[1]{
 \phantomsection
 \addcontentsline{toc}{section}{#1}
 {\large{\bfseries\color{accentText}#1} {\color{accentLine} |}}
}

\newcommand{\heading}[2]{
 \hspace{10pt}#1\hfill#2\\
}

\newcommand{\headingBf}[2]{
 \heading{\textbf{#1}}{\textbf{#2}}
}

\newcommand{\headingIt}[2]{
 \heading{\textit{#1}}{\textit{#2}}
}

\newenvironment{resume_list}{
 \vspace{-7pt}
 \begin{itemize}[itemsep=-2pt, parsep=1pt, leftmargin=26pt]
}{
 \end{itemize}
}

\renewcommand\labelitemi{--}

%% END_FILE: mteck.sty
%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%---------%
% Heading %
%---------%

\documentTitle{Muktha Ramesh}{
  \href{mailto:muktha21@mit.edu}{muktha21@mit.edu}  ~ | ~
  \href{tel:1234567890}{\raisebox{-0.05\height}(408)-637-0621}  ~ | ~
  \href{https://www.linkedin.com/in/muktharamesh28}{www.linkedin.com/in/muktharamesh28
} ~ | ~
  \href{https://github.com/muktharamesh20}{github.com/muktharamesh20
}
}



%---------%
% Education %
%---------%

\section{Education}
\headingBf{Massachusetts Institute of Technology (GPA: 5.0/5.0)}{Cambridge, MA}
\headingIt{Bachelor of Science in Computer Science}{Class of 2028}
\begin{resume_list}
  \item Introduction to Machine Learning, Discrete Mathematics, Introduction to Probability, Linear Algebra \& Optimization, Introduction to Algorithms, Computation Structures, Introduction to C and Assembly, Diffusion Models, LLMs from Scratch
\end{resume_list}


%---------%
% Skills %
%---------%
\section{Skills}
\vspace{-2pt}
\hspace{10pt}\textbf{Languages:} Python, C, Java, TypeScript/JavaScript, SQL/PostgreSQL, Julia \\
\hspace{10pt}\textbf{Frameworks:} React Native, Node.js, Express \\
\hspace{10pt}\textbf{ML Libraries:} Sklearn, PyTorch, Stable-Baselines, Tensorflow, OpenCV, Numpy, Pandas \\
\hspace{10pt}\textbf{Tools:} Git/GitHub, Docker, Linux, VS Code, ROS \\
\hspace{10pt}\textbf{Technical:} CAD (SolidWorks, Fusion 360), Robotics design, Database design, Data Structures + Algorithms, OOP \\

\section{Separated Machine Learning Projects}

\headingBf{MLP Controller for Robotic Pick-and-Place — PyTorch, MuJoCo}{Dec 2025 -- Jan 2026}
\begin{resume_list}
  \item Built an end-to-end MLP controller for a 7-DOF Franka Research 3 robot arm in MuJoCo, enabling autonomous pick-and-place task
  \item Generated a dataset of 10,000 expert trajectories and implemented multiple action space representations, providing a large-scale foundation for model training and evaluation
  \item Developed interactive visualization tools for trained policies and trajectory datasets, facilitating debugging and performance analysis
  \item Explored multiple MLP architectures (1024→1024→512→256→7 and smaller variants), balancing model complexity and generalization to refine manipulation strategies
\end{resume_list}

\headingBf{HKN Tutor at MIT}{Oct 2025 -- Present}
\begin{resume_list}
  \item Tutored two students in Intro to Machine Learning, covering the mathematical foundations of core ML models
  \item Explained loss functions and evaluation metrics underlying model training and assessment
\end{resume_list}



\headingBf{ML from Scratch — Python, NumPy}{Sep 2025 - Dec 2025}
\begin{resume_list}
  \item Implemented linear regression, binary and multi-class classifiers using gradient descent, SGD, cross-entropy, and NLL loss from scratch
  \item Built training and evaluation pipelines for these models, enabling experimentation with dataset size, learning rates, and optimization strategies
\end{resume_list}

\headingBf{Vehicle Segmentation Model — PyTorch}{Jan 2025}
\begin{resume_list}
  \item Built and trained a U-Net convolutional network for vehicle segmentation, achieving high-precision predictions on benchmark datasets
  \item Preprocessed and augmented image datasets to improve model generalization and robustness across varying lighting and perspectives
\end{resume_list}



%---------%
% Experience %
%---------%

\section{Competitions}

\headingBf{HackMIT Finalist}{Cambridge, MA}
\headingIt{HackMIT Hackathon - Oracle, React Native, n8n, PostgreSQL, Anthropic API, OAuth, Typescript}{September 2025}
\begin{resume_list}
  \item Competed in the Education track, designing and building a fully functional mobile app within 24 hours as a team of 3
  \item Developed a personalized language learning app which allows users to learn nearly any language and has an AI tutoring agent to adapt exercises and conversations to each learner’s level
  \item Implemented an onboarding system that collects learner preferences and goals
  \item Led the design of personalized vocabulary generation, integrating the Anthropic API to adapt content based on user level, goals, and learning history
  \item Drove the project from concept to deployment in a fast-paced hackathon environment; selected as a top 15 finalist out of 320 teams
\end{resume_list}
\headingBf{MIT Pokerbots Biggest Upset Winner}{Cambridge, MA}
\headingIt{MIT Pokerbots Competition — Python, Stable-Baselines3, PyTorch, TensorBoard}{January 2025}
\begin{resume_list}
 \item Developed a bot to play poker autonomously against 80 other bots in a multi-round tournament
  \item Developed a Python class to evaluate poker hands and board positions, forming the foundation for bot strategy
  \item Built reinforcement learning agents (Q-Learning, PPO, A2C) and a custom Gymnasium environment to train and test bots
  \item Collaborated with a team of 4, integrating common functions into a shared library, allowing for faster iteration
  \item Optimized RL agents with self-play to outperform 72\% of competitors, winning \$500 for the biggest upset
\end{resume_list}


\headingBf{\textbf{FIRST Robotics Team Captain - Java, Github}}{Hartford, CT}
\headingIt{Captain and Software Lead}{2021 – 2024}
\begin{resume_list}
\item Led a 30-member robotics team, advancing from local competitions to the World Championship
\item Redesigned codebase from a single file to modular subsystems, integrating path planning and control algorithms, improving maintainability and reliability
\item Streamlined the team's development pipeline by adopting a Kanban system
\end{resume_list}


\section{Experience}
\headingBf{Soft Drone Researcher}{Cambridge, MA}
\headingIt{MIT SPARK Labs - Python, ROS, Linux/Ubuntu}{August 2024 – January 2025}
\begin{resume_list}
  \item Implemented ROS and Python scripts on Ubuntu to enable precise drone camera rotation
  \item Designed and developed an improved aerial gripper, enhancing object grasping reliability and enabling potential dexterous aerial manipulation
  \item Investigated sensors and materials to optimize gripper feedback and improve control accuracy
\end{resume_list}


\headingBf{Competitive Mathematics Coach}{Cambridge MA}
\headingIt{Rastogi Mathemagicians Club}{September 2024 - December 2024}
\begin{resume_list}
    \item Developed curriculum and taught competitive mathematics to high school and middle school students
\end{resume_list}


\headingBf{Jane Street Academy of Math and Programming}{New York, NY}
\headingIt{Jane Street - Python}{June 2024 -- August 2024}
\begin{resume_list}
  \item Learned and applied combinatorics, number theory, graph theory, game theory, and computer science principles
  \item Designed AI agents for mathematically-focused games, developing algorithms to optimize performance.
  \item Applied object-oriented design principles, creative problem-solving, and rigorous testing.
    \item Gained insights into trading by participating in interactive trading games and Q\&A sessions with experienced traders.
\end{resume_list}

\headingBf{Robotics Intern}{Hartford, CT}
\headingIt{University of Hartford - CAD}{September 2023 -- June 2024}
\begin{resume_list}
  \item Collaborated with students to design and program a miniature humanoid robot for high school STEM engagement
  \item Defined project goals, user cases, and software requirements during the proposal phase
  \item Prototyped multiple motor configurations in CAD to optimize mobility and cost tradeoffs
\end{resume_list}


\headingBf{Website Developer}{Rocky Hill, CT}
\headingIt{Rocky Hill High School - Django, JavaScript, HTML, CSS, MongoDB}{2021 – 2024}
\begin{resume_list}
  \item Developed and maintained the World Language and Principal Newsletter websites, improving accessibility and content delivery of school news
  \item Designed a draft website for the school football program
  \item Led a team of 15 students in Principal Newsletter website development
  \item Finalist in the American Computer Science League competition
  \item Taught coding fundamentals to 30+ high school students, fostering early programming skills
\end{resume_list}


\headingBf{\textbf{Mathematics Team}}{Rocky Hill, CT} 
\headingIt{Captain}{2020-2024}
\begin{resume_list} 
  \item Taught competitive math and problem solving skills to 20 high school students.
  \item Led the team to 2nd place in the Capital Area Mathematics League and 3rd place in New England, improving from mid-standings among 25 teams in local competitions.
\end{resume_list} 

\headingBf{Robotics Camp Mentor}{Hartford, CT}
\headingIt{CT Science Center}{2022 – 2024}
\begin{resume_list}
  \item Developed a four-day robotics summer camp curriculum on coding, 3D printing, and STEM activities for 64 students
  \item Pitched and co-designed the camp program with a team of 5 to the CT Science Center
  \item Taught coding, 3D printing, and STEM concepts to students over four summer sessions, fostering hands-on learning
\end{resume_list}

\headingBf{Data Analysis \& Orbital Modeling \href{https://drive.google.com/file/d/13VIFkCziUaAo0zORf6v28rjzPFD_YXMA/view?usp=sharing}{[Research Paper Link]}}{Boulder, CO} 
\headingIt{Summer Science Program - Python, Bash/CLI, NumPy, Matplotlib} {June 2023 -- July 2023}
\begin{resume_list}
  \item Built Python pipelines to preprocess and align large datasets for quantitative analysis.
 \item Implemented Gauss’s Method to compute orbital elements, achieving $<0.1\%$ error vs NASA JPL Horizons.
  \item Executed 15,000+ iteration Monte Carlo simulations to quantify orbital uncertainty.
  \item Conducted statistical analysis (error propagation, standard deviation, z-tests) to validate results, producing high-precision orbit models.
  \item Published results to Minor Planet Center
\end{resume_list}


\headingBf{Machine Learning Projects — PyTorch, Python, NumPy, Pandas, TensorFlow}{Jan 2024 -- Present}
\begin{resume_list}
  \item Discuss recent ML research papers and real-world applications in the AI@MIT Reading Group weekly.
  \item Implemented linear regression, binary and multi-class classifiers, using GD/SGD, cross-entropy, and NLL loss from scratch (only Python).
  \item Tutored two students in 6.390 (Intro to Machine Learning) through HKN, covering core ML concepts.
  \item Trained neural networks in PyTorch and TensorFlow for handwritten digit and benchmark datasets.
  \item Implemented and trained GPT-2–style transformer architecture ($\sim$160M parameters) from scratch in PyTorch.
  \item Designed and trained an MLP controller for robotic pick-and-place manipulation tasks.
  \item Built and trained a PyTorch segmentation model for vehicle detection in images.
  \item Achieved 70\% accuracy in the Titanic Kaggle competition through feature engineering and model tuning.
\end{resume_list}




\section{Projects}
\headingBf{Group Travel Website - TypeScript, Vue, MongoDB}{Nov 2025 - Dec 2025}
\begin{resume_list}
  \item Built a travel planner with a cost splitter, packing list creator, and itenerary planner that works with groups.  
\end{resume_list}

\headingBf{Note Taking App - TypeScript, Vue, MongoDB}{Sept 2025 - Nov 2025}
\begin{resume_list}
  \item Built a note-taking app with automatic AI summarization and tagging.  
  \item Implemented regression testing, utilized modular monolithic architecture.
  \item \hyperlink{https://scriblink.onrender.com/login}{https://scriblink.onrender.com/login}
\end{resume_list}

\headingBf{Social Productivity App}{Rocky Hill, CT}
\headingIt{Self-Directed Project - PostgreSQL, TypeScript, React Native, GitHub, OAuth}{May 2025 -- Present}
\begin{resume_list}
  \item Designed and implemented a modular PostgreSQL backend with triggers, stored functions, and role-based access control to ensure secure and maintainable data handling.
  \item Developed automated unit and integration tests, enabling reliable code deployment and continuous integration, and fast debugging.
  \item Built frontend in React Native with recurring events, todos, and calendar scheduling, integrating backend APIs for seamless full-stack functionality.
 \item Implemented debouncing, caching, optimized SQL queries, pagination, and image size reduction to minimize database load, reduce network egress, and improve application performance.
  \item Applied OOP principles, version control, and CI/CD practices to ensure scalable, production-ready code.
\end{resume_list}

\headingBf{Movie Search \& Real-Time Trend Tracking App}{Rocky Hill, CT}
\headingIt{Self-Directed Project - SQL, TypeScript, React Native}{June 2025}
\begin{resume_list}
  \item Developed full-stack application integrating the TMDb API, tracking user interactions in a SQL database to support analytics and reporting.
  \item Implemented backend REST API with optimized queries and caching to enable high-throughput, low-latency performance.
  \item Built responsive frontend in TypeScript/React Native, connecting to backend services for real-time data display.
  \item Applied scalable architecture principles, modular code design, and maintainable software practices for production readiness.
\end{resume_list}


\headingBf{StarBattle Game –TypeScript, Git}{May 2025}
\begin{resume_list}
  \item Developed a web-based multiplayer strategy game with concurrent-safe code and automated unit and regression tests using Mocha, ensuring robust gameplay and fast debugging.
  \item Implemented game mechanics, backtracking algorithm to solve games, scoring logic, and multiple Abstract Data Types to support efficient and maintainable game design.
\end{resume_list}


\headingBf{Wordle Solver - Python}{2025}
\begin{resume_list}
  \item Built a Wordle-like game with a \textbf{tree-based search algorithm} to prune invalid guesses, reducing candidate words 80\% on average per turn.  
  \item Implemented an interactive solver that suggests optimal next moves, applying data structures for real-time word filtering.
\end{resume_list}


\headingBf{SAT Solver - Python}{2025}
\begin{resume_list}
  \item Implemented a \textbf{backtracking-based SAT solver} with heuristics for variable selection.  
  \item Optimized solver with unit propagation and pruning, successfully solving 100+ CNF benchmark instances.
\end{resume_list}



\headingBf{LISP Interpreter - Python}{May 2025}
\begin{resume_list}
  \item Developed a fully functional LISP interpreter in Python, supporting recursion, higher-order functions, and symbolic evaluation.  
  \item Designed modular architecture for extensibility, allowing integration of new operators with minimal changes.
\end{resume_list}

\headingBf{Symbolic Algebra Engine - Python}{2025}
\begin{resume_list}
  \item Created a program to perform \textbf{symbolic differentiation and simplification} of algebraic expressions.  
  \item Implemented expression trees for efficient manipulation, enabling operations such as factoring and expansion.
\end{resume_list}




%---------%
% Awards %
%---------%
\section{Other Awards}
\vspace{-2pt}
\hspace{10pt}\textbf{ARML Connecticut Representative (2x):} Represented Connecticut in the nation’s top high school math team competition \\
\hspace{10pt}\textbf{AIME Qualifier (2x):} Placed in the top 2.5\% nationwide on the American Mathematics Competition to advance to AIME \\
\hspace{10pt}\textbf{Connecticut All-State Robotics (2x):} Recognized among the top 36 robotics leaders in Connecticut in high school\\
\hspace{10pt}\textbf{American Computer Science League Finalist:} Advanced to finals through top performance in programming and CS contests \\
\hspace{10pt}\textbf{FIRST Robotics Dean's List Semi-finalist:} Honored for leadership, expertise, and impact in the robotics community \\






\end{document}
