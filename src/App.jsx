import { useState } from 'react'
import './App.css'

/* =========================================================
   EDUPRO RESOURCE DATA
   ========================================================= */

const DRIVE_ROOT =
  'https://drive.google.com/drive/folders/1BSRgzkqGgpJ9oZuzfSfa5QNTXVEsf4E4?usp=drive_link'

const semester1Subjects = [
  {
    title: 'BEEE',
    fullName: 'Basic Electrical and Electronics Engineering',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '⚡',
    color: 'blue-resource',
    description:
      'Electrical circuits, electronic components, electrical machines, measurements and basic electrical engineering concepts.',
    tags: ['Circuits', 'Electronics', 'Electrical'],
    practical: true
  },

  {
    title: 'Communicative English',
    fullName: 'Communicative English',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '📚',
    color: 'purple-resource',
    description:
      'English communication, grammar, vocabulary, professional communication, presentations and writing skills.',
    tags: ['English', 'Communication', 'Grammar'],
    practical: false
  },

  {
    title: 'Engineering Chemistry',
    fullName: 'Engineering Chemistry',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '🧪',
    color: 'green-resource',
    description:
      'Engineering chemistry concepts including materials, water chemistry, corrosion, polymers, fuels and industrial chemistry.',
    tags: ['Chemistry', 'Materials', 'Engineering'],
    practical: true
  },

  {
    title: 'Engineering Mechanics',
    fullName: 'Engineering Mechanics',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '⚙️',
    color: 'orange-resource',
    description:
      'Forces, equilibrium, friction, moments, beams, motion and fundamental engineering mechanics concepts.',
    tags: ['Mechanics', 'Forces', 'Engineering'],
    practical: true
  },

  {
    title: 'Python Programming',
    fullName: 'Python Programming',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '🐍',
    color: 'blue-resource',
    description:
      'Python programming fundamentals, variables, control structures, functions, data structures and problem solving.',
    tags: ['Python', 'Programming', 'Coding'],
    practical: true
  },

  {
    title: 'SMVC',
    fullName: 'SMVC',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '🎓',
    color: 'purple-resource',
    description:
      'Study resources, notes, lectures and examination material for the SMVC subject.',
    tags: ['SMVC', 'Theory', 'Exams'],
    practical: false
  },

  {
    title: 'Workshop Practices',
    fullName: 'Workshop Practices',
    semester: 'Semester 1',
    year: '1st Year',
    icon: '🔧',
    color: 'orange-resource',
    description:
      'Hands-on workshop practices, tools, manufacturing processes, safety procedures and practical engineering skills.',
    tags: ['Workshop', 'Practical', 'Engineering'],
    practical: true
  }
]

const semester2Subjects = [
  {
    title: 'Building Programming Logic in C',
    fullName: 'Building Programming Logic in C',
    semester: 'Semester 2',
    year: '1st Year',
    icon: '💻',
    color: 'blue-resource',
    description:
      'C programming fundamentals, programming logic, algorithms, control structures, functions, arrays and problem solving.',
    tags: ['C', 'Programming', 'Logic'],
    practical: true
  },

  {
    title: 'Engineering Graphics',
    fullName: 'EG Engineering Graphics',
    semester: 'Semester 2',
    year: '1st Year',
    icon: '📐',
    color: 'green-resource',
    description:
      'Engineering drawing, projections, geometric constructions, sections, development and graphical representation.',
    tags: ['Graphics', 'Drawing', 'Design'],
    practical: true
  },

  {
    title: 'Engineering Physics',
    fullName: 'EP Engineering Physics',
    semester: 'Semester 2',
    year: '1st Year',
    icon: '🔬',
    color: 'blue-resource',
    description:
      'Physics concepts applied to engineering including mechanics, waves, optics, materials and modern physics.',
    tags: ['Physics', 'Science', 'Engineering'],
    practical: true
  },

  {
    title: 'Indian Knowledge System',
    fullName: 'IKS Indian Knowledge System',
    semester: 'Semester 2',
    year: '1st Year',
    icon: '🇮🇳',
    color: 'orange-resource',
    description:
      'Indian Knowledge System, traditional knowledge, science, mathematics, technology, philosophy and cultural heritage.',
    tags: ['IKS', 'Knowledge', 'Culture'],
    practical: false
  },

  {
    title: 'Linear Algebra and Differential Equations',
    fullName: 'LADE Linear Algebra and Differential Equations',
    semester: 'Semester 2',
    year: '1st Year',
    icon: '📐',
    color: 'purple-resource',
    description:
      'Matrices, vectors, linear equations, eigenvalues, eigenvectors and differential equations for engineering applications.',
    tags: ['Mathematics', 'Algebra', 'Differential Equations'],
    practical: false
  },

  {
    title: 'Recent Trends in Integrated Technology',
    fullName: 'RTIT Recent Trends in Integrated Technology',
    semester: 'Semester 2',
    year: '1st Year',
    icon: '🚀',
    color: 'green-resource',
    description:
      'Emerging technologies, modern engineering trends, digital technologies and recent developments in integrated technology.',
    tags: ['Technology', 'Innovation', 'Trends'],
    practical: false
  }
]

const allSubjects = [
  ...semester1Subjects,
  ...semester2Subjects
]

/* =========================================================
   ACTUAL DRIVE RESOURCE DATA
   ========================================================= */

const epResources = [
  { title: '01 Modern Physics Electron Optics', url: 'https://drive.google.com/open?id=13kyqg1xD-0QPYQZYVCkuWQsmh_kajOGJ&usp=drive_copy', type: 'Topic' },
  { title: '02 Wave Optics Interference', url: 'https://drive.google.com/open?id=1Q6zHzd2a-6Z_7ib9S_mQnvHDUgVXPLsv&usp=drive_copy', type: 'Topic' },
  { title: '03 Materials of Technological Importance Dielectric Materials', url: 'https://drive.google.com/open?id=1pbDzLWncbKnG22MluqrZ2vXjUwJHGB00&usp=drive_copy', type: 'Topic' },
  { title: '04 Optoelectronic Materials and Devices LASER', url: 'https://drive.google.com/open?id=1dWC8r1eho5MeI1vbONrN_ntxV8CKRNKd&usp=drive_copy', type: 'Topic' },
  { title: '05 Physics of Materials', url: 'https://drive.google.com/open?id=1TnSHp7LfFcPHloSMsoNep2-Ghj25ldLE&usp=drive_copy', type: 'Topic' },
  { title: 'EP Practical', url: 'https://drive.google.com/open?id=1eOEz6y2bbxoTeNLoGXyrfe8AdqFA_Dkk&usp=drive_copy', type: 'Practical' },
  { title: 'EP PYQ and Question Bank', url: 'https://drive.google.com/open?id=1c67Mzwp_HNYN1ARgsnEvsyFcycyii4le&usp=drive_copy', type: 'Previous Papers' },
  { title: 'EP Senior Notes', url: 'https://drive.google.com/open?id=10UGuVVghsHlmb_CZOXUVYrTiiwBTQIkk&usp=drive_copy', type: 'Notes & PDFs' },
  { title: 'EP WorkBook', url: 'https://drive.google.com/open?id=1k_qzUxLn6DcCsUq5HtVFafOrnCxqSkYq&usp=drive_copy', type: 'Notes & PDFs' },
  { title: 'Reference Books', url: 'https://drive.google.com/open?id=1-yo79T2RDdszvGrzH1vswxVdM1bEDFmL&usp=drive_copy', type: 'Notes & PDFs' },
  { title: 'Syllabus', url: 'https://drive.google.com/open?id=1UYnpbABKdX8DKGs1xKK_tQgxvAAEkkfm&usp=drive_copy', type: 'Notes & PDFs' },
  { title: 'EP End Sem Imp Points.pdf', url: 'https://drive.google.com/open?id=10kF1D-lp2IksJ_sirDP_Dj3Y1OYXB8b6&usp=drive_copy', type: 'Exam Preparation' },
  { title: 'EP Practice Questions 2024-25.pdf', url: 'https://drive.google.com/open?id=1omTDbK5841N8Z8ufATujQ0UDg3JP14AB&usp=drive_copy', type: 'Exam Preparation' },
  { title: 'Physics QBank 24-25 Numerical Solutions.pdf', url: 'https://drive.google.com/open?id=1xVZkmaosYKuF-aZwnliLgjMTCvbc77AO&usp=drive_copy', type: 'Exam Preparation' }
]

const pythonResources = [
  {
    title: 'Python Programming — Chapter 1',
    url: '/resources/Python_Programming_Chapter_1.pdf',
    type: 'Notes & PDFs'
  }
]

const subjectResources = {
  'Engineering Physics': epResources
}

/* =========================================================
   APP
   ========================================================= */


function App() {
  const [showLearningPath, setShowLearningPath] = useState(false)

  const [resourceFilter, setResourceFilter] =
    useState('All Resources')

  const [resourceSearch, setResourceSearch] =
    useState('')

  const [semesterFilter, setSemesterFilter] =
    useState('All Semesters')

  const [selectedResource, setSelectedResource] =
    useState(null)

  /* =======================================================
     FILTER SUBJECTS
     ======================================================= */

  const filteredSubjects = allSubjects.filter((subject) => {
    const matchesSemester =
      semesterFilter === 'All Semesters' ||
      subject.semester === semesterFilter

    const searchText = `
      ${subject.title}
      ${subject.fullName}
      ${subject.semester}
      ${subject.description}
      ${subject.tags.join(' ')}
    `.toLowerCase()

    const matchesSearch =
      searchText.includes(resourceSearch.toLowerCase())

    return matchesSemester && matchesSearch
  })

  /* =======================================================
     CHECK RESOURCE FILTER
     ======================================================= */

  const shouldShowSubject = (subject) => {
    if (resourceFilter === 'All Resources') return true

    const resources = subjectResources[subject.title] || []

    if (resourceFilter === 'YouTube') return false

    if (resourceFilter === 'Notes & PDFs') {
      return resources.some((r) => r.type === 'Notes & PDFs')
    }

    if (resourceFilter === 'Previous Papers') {
      return resources.some((r) => r.type === 'Previous Papers')
    }

    if (resourceFilter === 'Practical') {
      return resources.some((r) => r.type === 'Practical')
    }

    return resources.some((r) => r.type === resourceFilter)
  }

  const visibleSubjects =
    filteredSubjects.filter(shouldShowSubject)

  return (
    <div className="app">

      {/* ===================================================
          NAVBAR
      =================================================== */}

      <nav className="navbar">

        <div className="logo">
          Edu<span>Pro</span>
        </div>

        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#resources">Resources</a>
          <a href="#mentors">Mentors</a>
          <a href="#career">Career</a>
          <a href="#about">About</a>
        </div>

        <button className="login-btn">
          Login
        </button>

      </nav>


      {/* ===================================================
          HERO SECTION
      =================================================== */}

      <section className="hero-section" id="home">

        <div className="hero-content">

          <p className="small-heading">
            🎓 Your Complete Student Career Platform
          </p>

          <h1>
            Learn. Connect. <span>Grow.</span>
          </h1>

          <p className="hero-text">
            EduPro connects students with study resources,
            experienced seniors, mentorship and career
            opportunities — all in one place.
          </p>

          <div className="hero-buttons">

            <button
              className="primary-btn"
              onClick={() =>
                document
                  .getElementById('resources')
                  ?.scrollIntoView({
                    behavior: 'smooth'
                  })
              }
            >
              Get Started →
            </button>

            <button
              className="secondary-btn"
              onClick={() =>
                document
                  .getElementById('resources')
                  ?.scrollIntoView({
                    behavior: 'smooth'
                  })
              }
            >
              Explore Resources
            </button>

          </div>

          <div className="hero-stats">

            <div>
              <h3>13+</h3>
              <p>Subjects</p>
            </div>

            <div>
              <h3>4</h3>
              <p>Resource Types</p>
            </div>

            <div>
              <h3>2</h3>
              <p>Semesters</p>
            </div>

          </div>

        </div>


        <div className="hero-card">

          <div className="card-header">

            <div className="profile-circle">
              👩‍🎓
            </div>

            <div>
              <h3>Student Dashboard</h3>
              <p>Your learning journey</p>
            </div>

          </div>


          <div className="progress-box">

            <div className="progress-title">
              <span>Learning Progress</span>
              <strong>78%</strong>
            </div>

            <div className="progress-bar">
              <div className="progress-fill"></div>
            </div>

          </div>


          <div className="dashboard-items">

            <div className="dashboard-item">

              <span>📚</span>

              <div>
                <strong>Study Resources</strong>
                <small>
                  Sem 1 & Sem 2 subjects
                </small>
              </div>

            </div>


            <div className="dashboard-item">

              <span>👨‍🏫</span>

              <div>
                <strong>Mentorship</strong>
                <small>3 mentors available</small>
              </div>

            </div>


            <div className="dashboard-item">

              <span>💼</span>

              <div>
                <strong>Career Preparation</strong>
                <small>Skills to improve</small>
              </div>

            </div>

          </div>

        </div>

      </section>


      {/* ===================================================
          STUDY RESOURCES
      =================================================== */}

      <section
        className="resources-section"
        id="resources"
      >

        <div className="section-heading">

          <p>LEARN SMARTER</p>

          <h2>
            Your Study Resources,
            <span> All in One Place</span>
          </h2>

          <p className="section-description">
            Explore your actual Semester 1 and Semester 2
            subjects with notes, videos, previous-year papers
            and practical resources.
          </p>

        </div>


        {/* SEARCH */}

        <div className="resource-search">

          <span>🔎</span>

          <input
            type="text"
            placeholder="Search subjects, topics or resources..."
            value={resourceSearch}
            onChange={(e) =>
              setResourceSearch(e.target.value)
            }
          />

          {resourceSearch && (

            <button
              className="clear-search"
              onClick={() =>
                setResourceSearch('')
              }
            >
              ✕
            </button>

          )}

        </div>


        {/* SEMESTER FILTER */}

        <div className="resource-filters">

          {[
            'All Semesters',
            'Semester 1',
            'Semester 2'
          ].map((semester) => (

            <button
              key={semester}
              className={`resource-filter ${
                semesterFilter === semester
                  ? 'active'
                  : ''
              }`}
              onClick={() =>
                setSemesterFilter(semester)
              }
            >
              {semester}
            </button>

          ))}

        </div>


        {/* RESOURCE FILTERS */}

        <div className="resource-filters">

          {[
            'All Resources',
            'Notes & PDFs',
            'YouTube',
            'Previous Papers',
            'Practical'
          ].map((filter) => (

            <button
              key={filter}
              className={`resource-filter ${
                resourceFilter === filter
                  ? 'active'
                  : ''
              }`}
              onClick={() =>
                setResourceFilter(filter)
              }
            >
              {filter}
            </button>

          ))}

        </div>


        {/* RESULT INFO */}

        <div className="resource-result-info">

          <strong>
            {visibleSubjects.length} Subjects Available
          </strong>

          <span>
            {semesterFilter} • {resourceFilter}
            {' • '}
            Search results update instantly
          </span>

        </div>


        {/* =================================================
            RESOURCE CARDS
        ================================================= */}

        <div className="resources-container">

          {visibleSubjects.length > 0 ? (

            visibleSubjects.map((subject) => (

              <div
                className="resource-card"
                key={subject.title}
              >

                <div
                  className={`resource-icon ${subject.color}`}
                >
                  {subject.icon}
                </div>

                <div className="resource-content">

                  <span className="resource-year">
                    {subject.semester}
                  </span>

                  <h3>
                    {subject.title}
                  </h3>

                  <p>
                    {subject.description}
                  </p>


                  <div className="resource-meta">
                    {(subjectResources[subject.title] || []).length > 0 ? (
                      [...new Set((subjectResources[subject.title] || []).map((r) => r.type))].map((type) => (
                        <span key={type}>
                          {type === 'Practical' ? '💻' : type === 'Previous Papers' ? '📝' : type === 'Exam Preparation' ? '🎯' : '📄'} {type}
                        </span>
                      ))
                    ) : (
                      <span>🔗 Actual Drive links pending</span>
                    )}
                  </div>


                  <button
                    className="resource-btn"
                    onClick={() =>
                      setSelectedResource(subject)
                    }
                  >
                    Explore Resources →
                  </button>

                </div>

              </div>

            ))

          ) : (

            <div
              style={{
                width: '100%',
                textAlign: 'center',
                padding: '50px 20px'
              }}
            >

              <div
                style={{
                  fontSize: '50px',
                  marginBottom: '15px'
                }}
              >
                🔍
              </div>

              <h3>
                No subjects found
              </h3>

              <p>
                Try another subject name or change the
                filters.
              </p>

            </div>

          )}

        </div>


        {/* =================================================
            RESOURCE EXPLORER MODAL
        ================================================= */}

        {selectedResource && (

          <div className="resource-modal-overlay">

            <div className="resource-modal">

              <button
                className="resource-modal-close"
                onClick={() =>
                  setSelectedResource(null)
                }
              >
                ✕
              </button>


              <div className="resource-modal-icon">
                {selectedResource.icon}
              </div>

              <span className="resource-modal-year">
                {selectedResource.semester}
              </span>

              <h2>
                {selectedResource.title}
              </h2>

              <p className="resource-modal-description">
                {selectedResource.description}
              </p>


              {/* =================================================
                  ACTUAL DRIVE RESOURCE OPTIONS
              ================================================= */}

              <div className="resource-options">
                {(subjectResources[selectedResource.title] || []).length > 0 ? (
                  (subjectResources[selectedResource.title] || []).map((resource) => (
                    <a
                      key={resource.title}
                      className="resource-option"
                      href={resource.url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <span>
                        {resource.type === 'Practical'
                          ? '💻'
                          : resource.type === 'Previous Papers'
                            ? '📝'
                            : resource.type === 'Exam Preparation'
                              ? '🎯'
                              : '📄'}
                      </span>

                      <div>
                        <strong>{resource.title}</strong>
                        <small>{resource.type} • Open Google Drive</small>
                      </div>
                    </a>
                  ))
                ) : (
                  <div style={{ padding: '20px', textAlign: 'center' }}>
                    <strong>Actual Drive resources not added yet</strong>
                    <p style={{ marginTop: '8px' }}>
                      No resource link has been provided for this subject yet.
                    </p>
                  </div>
                )}
              </div>


              <button
                className="resource-modal-back"
                onClick={() =>
                  setSelectedResource(null)
                }
              >
                ← Back to Resources
              </button>

            </div>

          </div>

        )}

      </section>


      {/* ===================================================
          HOW EDUPRO WORKS
      =================================================== */}

      <section className="how-section">

        <div className="section-heading">

          <p>HOW EDUPRO WORKS</p>

          <h2>
            Your Journey from Learning to <span>Career</span>
          </h2>

          <p className="section-description">
            EduPro brings learning, mentorship and career
            preparation together in a simple student journey.
          </p>

        </div>


        <div className="steps-container">

          <div className="step-card">

            <span className="step-number">
              01
            </span>

            <div className="step-icon">
              🔍
            </div>

            <h3>
              Discover
            </h3>

            <p>
              Find subject-wise notes, videos, previous year
              papers and resources based on your academic needs.
            </p>

          </div>


          <div className="step-card">

            <span className="step-number">
              02
            </span>

            <div className="step-icon">
              📖
            </div>

            <h3>
              Learn
            </h3>

            <p>
              Learn from curated resources and build strong
              academic and technical foundations.
            </p>

          </div>


          <div className="step-card">

            <span className="step-number">
              03
            </span>

            <div className="step-icon">
              🤝
            </div>

            <h3>
              Connect
            </h3>

            <p>
              Connect with experienced seniors for guidance
              on projects, internships, skills and placements.
            </p>

          </div>


          <div className="step-card">

            <span className="step-number">
              04
            </span>

            <div className="step-icon">
              🚀
            </div>

            <h3>
              Grow
            </h3>

            <p>
              Identify skill gaps, improve your profile and
              prepare for your future career.
            </p>

          </div>

        </div>

      </section>


      {/* ===================================================
          SENIOR MENTORSHIP
      =================================================== */}

      <section
        className="mentorship-section"
        id="mentors"
      >

        <div className="section-heading">

          <p>SENIOR MENTORSHIP</p>

          <h2>
            Learn from <span>Experienced Seniors</span>
          </h2>

          <p className="section-description">
            Get practical guidance from seniors who have
            already experienced college projects, internships
            and placements.
          </p>

        </div>


        <div className="mentorship-container">


          <div className="mentorship-intro">

            <div className="mentor-main-icon">
              👨‍🏫
            </div>

            <h3>
              Real Guidance. Real Experience.
            </h3>

            <p>
              Connect with seniors for help with academics,
              projects, internships, placements and career
              decisions.
            </p>

            <div className="mentor-topics">
              <span>📚 Academics</span>
              <span>💻 Projects</span>
              <span>🎯 Placements</span>
              <span>💼 Internships</span>
            </div>

          </div>


          <div className="mentor-list">


            <div className="mentor-card">

              <div className="mentor-avatar">
                👨‍💻
              </div>

              <div className="mentor-info">

                <div className="mentor-name-row">

                  <div>

                    <h3>
                      Rahul Sharma
                    </h3>

                    <p>
                      Software Engineer · 2 Years Experience
                    </p>

                  </div>

                  <span className="mentor-rating">
                    ⭐ 4.9
                  </span>

                </div>


                <div className="mentor-tags">
                  <span>DSA</span>
                  <span>Python</span>
                  <span>Placements</span>
                </div>


                <p className="mentor-experience">
                  Helps students prepare for technical
                  interviews, coding rounds and software
                  development careers.
                </p>


                <button className="mentor-btn">
                  View Profile →
                </button>

              </div>

            </div>


            <div className="mentor-card">

              <div className="mentor-avatar purple-avatar">
                👩‍💻
              </div>

              <div className="mentor-info">

                <div className="mentor-name-row">

                  <div>

                    <h3>
                      Priya Deshmukh
                    </h3>

                    <p>
                      Data Analyst · 3 Years Experience
                    </p>

                  </div>

                  <span className="mentor-rating">
                    ⭐ 4.8
                  </span>

                </div>


                <div className="mentor-tags">
                  <span>SQL</span>
                  <span>Python</span>
                  <span>Data Analytics</span>
                </div>


                <p className="mentor-experience">
                  Guides students on data analytics projects,
                  internships and industry-ready skills.
                </p>


                <button className="mentor-btn">
                  View Profile →
                </button>

              </div>

            </div>

          </div>

        </div>

      </section>


      {/* ===================================================
          CAREER INTELLIGENCE
      =================================================== */}

      <section
        className="career-section"
        id="career"
      >

        <div className="section-heading">

          <p>CAREER INTELLIGENCE</p>

          <h2>
            Know Your Skills. <span>Build Your Future.</span>
          </h2>

          <p className="section-description">
            EduPro analyzes your skills, learning progress
            and career goals to help you understand what to
            improve next.
          </p>

        </div>


        <div className="career-container">


          {/* SKILL ANALYSIS */}

          <div className="career-card">

            <div className="career-icon">
              📊
            </div>

            <h3>
              Skill Analysis
            </h3>

            <p>
              Understand your current technical skills and
              identify areas where you need more practice.
            </p>


            <div className="skill-item">

              <div className="skill-header">
                <span>Python</span>
                <strong>85%</strong>
              </div>

              <div className="skill-bar">
                <div
                  className="skill-fill"
                  style={{ width: '85%' }}
                ></div>
              </div>

            </div>


            <div className="skill-item">

              <div className="skill-header">
                <span>SQL</span>
                <strong>72%</strong>
              </div>

              <div className="skill-bar">
                <div
                  className="skill-fill"
                  style={{ width: '72%' }}
                ></div>
              </div>

            </div>


            <div className="skill-item">

              <div className="skill-header">
                <span>DSA</span>
                <strong>60%</strong>
              </div>

              <div className="skill-bar">
                <div
                  className="skill-fill"
                  style={{ width: '60%' }}
                ></div>
              </div>

            </div>

          </div>


          {/* PLACEMENT READINESS */}

          <div className="career-card readiness-card">

            <div className="career-icon green-career-icon">
              🎯
            </div>

            <h3>
              Placement Readiness
            </h3>

            <p>
              Track how prepared you are for internships
              and placement opportunities.
            </p>


            <div className="readiness-score">

              <strong>
                78%
              </strong>

              <span>
                Ready
              </span>

            </div>


            <div className="readiness-items">

              <div>
                <span>✓</span>
                Resume
              </div>

              <div>
                <span>✓</span>
                Technical Skills
              </div>

              <div>
                <span>✓</span>
                Projects
              </div>

              <div>
                <span>!</span>
                Aptitude Practice
              </div>

            </div>

          </div>


          {/* PERSONALIZED GUIDANCE */}

          <div className="career-card recommendation-card">

            <div className="career-icon purple-career-icon">
              🤖
            </div>

            <h3>
              Personalized Guidance
            </h3>

            <p>
              Get recommendations based on your skills,
              interests and career goals.
            </p>


            <div className="recommendation-box">

              <strong>
                Recommended for you
              </strong>

              <p>
                Improve SQL and DSA skills before your next
                placement assessment.
              </p>


              <button
                className="recommendation-btn"
                onClick={() =>
                  setShowLearningPath(
                    !showLearningPath
                  )
                }
              >
                {showLearningPath
                  ? 'Hide Learning Path ↑'
                  : 'View Learning Path →'}
              </button>


              {showLearningPath && (

                <div className="learning-path">

                  <strong>
                    Your Recommended Learning Path
                  </strong>

                  <p>
                    1. Strengthen SQL fundamentals
                  </p>

                  <p>
                    2. Practice DSA problem solving
                  </p>

                  <p>
                    3. Build one SQL-based project
                  </p>

                  <p>
                    4. Practice aptitude and technical interviews
                  </p>

                </div>

              )}

            </div>

          </div>

        </div>


        {/* CAREER CTA */}

        <div className="career-highlight">

          <div>

            <strong>
              Build a personalized career roadmap
            </strong>

            <p>
              EduPro can combine your learning activity,
              skills and goals to recommend resources,
              mentors and career opportunities.
            </p>

          </div>

          <button className="primary-btn">
            Explore My Career →
          </button>

        </div>

      </section>


      {/* ===================================================
          ABOUT
      =================================================== */}

      <section
        id="about"
        style={{
          padding: '80px 7%',
          textAlign: 'center',
          background: 'white'
        }}
      >

        <div className="section-heading">

          <p>ABOUT EDUPRO</p>

          <h2>
            Learn. Connect. <span>Grow.</span>
          </h2>

          <p className="section-description">
            EduPro is designed to bring academic resources,
            senior mentorship and career intelligence together
            for students.
          </p>

        </div>

      </section>

    </div>
  )
}

export default App