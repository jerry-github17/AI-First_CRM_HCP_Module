import InteractionForm from "./components/InteractionForm";
import ChatBox from "./components/ChatBox";
import "./App.css";

function App() {
  return (
    <main className="app">
      <header className="app-header">
        <h1>Log HCP Interaction</h1>
      </header>

      <div className="dashboard">
        <section className="form-panel">
          <InteractionForm />
        </section>

        <section className="chat-panel">
          <ChatBox />
        </section>
      </div>
    </main>
  );
}

export default App;