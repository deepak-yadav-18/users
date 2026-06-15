import "./MyCSS.css"
function Dashboard() {
  const stats = [
    { title: "Users", value: "12,940", color: "#b71556" },
    { title: "Revenue", value: "$48,200", color: "#10b981" },
    { title: "Orders", value: "1,245", color: "#f0c984" },
    { title: "Growth", value: "+18%", color: "#c2aeef" },
  ];

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="header">
        <div>
          <h1>Dashboard</h1>
          <p>Welcome back 👋</p>
        </div>

        <button className="btn">+ New Report</button>
      </header>

      {/* Stats */}
      <section className="stats-grid">
        {stats.map((item,index) => (
          <div className="card" key={item.title}>
            <h3>{item.title}</h3>
            <h2 style={{ color: item.color }}>{item.value}</h2>
          </div>
        ))}
      </section>

      {/* Main Content */}
      <section className="content-grid">
        <div className="card large-card">
          <h3>Analytics Overview</h3>
          <div className="chart-placeholder">
            📊 Chart Area
          </div>
        </div>

        <div className="card">
          <h3>Recent Activity</h3>
          <ul className="activity-list">
            <li>User John signed up</li>
            <li>New order #1245 received</li>
            <li>Revenue increased by 8%</li>
            <li>Server backup completed</li>
          </ul>
        </div>
      </section>
    </div>
  );
}

export default Dashboard;