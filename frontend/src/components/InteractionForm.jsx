import { useState, useEffect } from "react";
import api from "../api/axios";
import { useDispatch, useSelector } from "react-redux";
import { addInteraction } from "../features/interactions/interactionSlice";

function InteractionForm() {
    const dispatch = useDispatch();

    const selectedInteraction = useSelector(
        (state) => state.interactions.selectedInteraction
    );

    const initialForm = {
        hcp_name: "",
        interaction_type: "",
        interaction_date: "",
        attendees: "",
        summary: "",
        materials_shared: "",
        samples_distributed: "",
        sentiment: "",
        outcome: "",
        follow_up_action: "",
        follow_up_date: ""
    };

    const [form, setForm] = useState(initialForm);

    const formatDateTimeLocal = (value) => {
        if (!value || value === "None" || value === "null") {
            return "";
        }

        return value.replace(" ", "T").slice(0, 16);
    };

    useEffect(() => {
        if (!selectedInteraction) return;

        setForm({
            hcp_name: selectedInteraction.hcp_name || "",
            interaction_type:
                selectedInteraction.interaction_type || "",
            interaction_date: formatDateTimeLocal(
                selectedInteraction.interaction_date
            ),
            attendees: selectedInteraction.attendees || "",
            summary: selectedInteraction.summary || "",
            materials_shared:
                selectedInteraction.materials_shared || "",
            samples_distributed:
                selectedInteraction.samples_distributed || "",
            sentiment: selectedInteraction.sentiment || "",
            outcome: selectedInteraction.outcome || "",
            follow_up_action:
                selectedInteraction.follow_up_action || "",
            follow_up_date: formatDateTimeLocal(
                selectedInteraction.follow_up_date
            )
        });
    }, [selectedInteraction]);

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        });
    };

    const addMaterial = () => {
        const material = prompt("Enter material shared:");

        if (material?.trim()) {
            setForm((prev) => ({
                ...prev,
                materials_shared: material.trim()
            }));
        }
    };

    const addSample = () => {
        const sample = prompt("Enter sample distributed:");

        if (sample?.trim()) {
            setForm((prev) => ({
                ...prev,
                samples_distributed: sample.trim()
            }));
        }
    };

    const submitHandler = async (e) => {
        e.preventDefault();

        try {
            const formattedForm = {
                ...form,

                interaction_date: form.interaction_date
                    ? form.interaction_date.replace("T", " ") + ":00"
                    : null,

                follow_up_date: form.follow_up_date
                    ? form.follow_up_date.replace("T", " ") + ":00"
                    : null
            };

            const response = await api.post(
                "/interactions/",
                formattedForm
            );

            dispatch(addInteraction(response.data));

            alert("Interaction logged successfully");

            setForm(initialForm);

        } catch (error) {
            console.error(
                "SUBMIT ERROR:",
                error.response?.data || error
            );

            alert(
                JSON.stringify(
                    error.response?.data || error.message
                )
            );
        }
    };

    return (
        <form
            className="interaction-form"
            onSubmit={submitHandler}
        >
            <h1>Log HCP Interaction</h1>

            <div className="section-title">
                Interaction Details
            </div>

            <div className="form-row">
                <div className="form-group">
                    <label>HCP Name</label>
                    <input
                        name="hcp_name"
                        placeholder="Search or select HCP..."
                        value={form.hcp_name}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Interaction Type</label>

                    <select
                        name="interaction_type"
                        value={form.interaction_type}
                        onChange={handleChange}
                        required
                    >
                        <option value="">
                            Select interaction type
                        </option>

                        <option value="Meeting">
                            Meeting
                        </option>

                        <option value="Call">
                            Call
                        </option>

                        <option value="Email">
                            Email
                        </option>

                        <option value="Conference">
                            Conference
                        </option>

                        {form.interaction_type &&
                            ![
                                "Meeting",
                                "Call",
                                "Email",
                                "Conference"
                            ].includes(form.interaction_type) && (
                                <option value={form.interaction_type}>
                                    {form.interaction_type}
                                </option>
                            )}
                    </select>
                </div>
            </div>

            <div className="form-row">
                <div className="form-group">
                    <label>
                        Interaction Date & Time
                    </label>

                    <input
                        type="datetime-local"
                        name="interaction_date"
                        value={form.interaction_date}
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label>
                        Follow-up Date & Time
                    </label>

                    <input
                        type="datetime-local"
                        name="follow_up_date"
                        value={form.follow_up_date}
                        onChange={handleChange}
                    />
                </div>
            </div>

            <div className="form-group">
                <label>Attendees</label>

                <input
                    name="attendees"
                    placeholder="Enter names or search..."
                    value={form.attendees}
                    onChange={handleChange}
                />
            </div>

            <div className="form-group">
                <label>Topics Discussed</label>

                <textarea
                    name="summary"
                    placeholder="Enter key discussion points..."
                    value={form.summary}
                    onChange={handleChange}
                    required
                />
            </div>

            <div className="voice-summary">
                🎙 Summarize from Voice Note (Requires Consent)
            </div>

            <div className="section-title">
                Materials Shared / Samples Distributed
            </div>

            <div className="resource-section">
                <label>Materials Shared</label>

                <div className="resource-row">
                    <span>
                        {form.materials_shared ||
                            "No materials added."}
                    </span>

                    <button
                        type="button"
                        className="small-action-button"
                        onClick={addMaterial}
                    >
                        🔍 Search/Add
                    </button>
                </div>
            </div>

            <div className="resource-section">
                <label>Samples Distributed</label>

                <div className="resource-row">
                    <span>
                        {form.samples_distributed ||
                            "No samples added."}
                    </span>

                    <button
                        type="button"
                        className="small-action-button"
                        onClick={addSample}
                    >
                        + Add Sample
                    </button>
                </div>
            </div>

            <div className="form-group sentiment-group">
                <label>
                    Observed/Inferred HCP Sentiment
                </label>

                <div className="sentiment-options">
                    {["Positive", "Neutral", "Negative"].map(
                        (sentiment) => (
                            <label key={sentiment}>
                                <input
                                    type="radio"
                                    name="sentiment"
                                    value={sentiment}
                                    checked={
                                        form.sentiment === sentiment
                                    }
                                    onChange={handleChange}
                                />
                                {sentiment}
                            </label>
                        )
                    )}
                </div>
            </div>

            <div className="form-group">
                <label>Outcomes</label>

                <textarea
                    name="outcome"
                    placeholder="Key outcomes or agreements..."
                    value={form.outcome}
                    onChange={handleChange}
                />
            </div>

            <div className="form-group">
                <label>Follow-up Actions</label>

                <textarea
                    name="follow_up_action"
                    placeholder="Enter next steps or tasks..."
                    value={form.follow_up_action}
                    onChange={handleChange}
                />
            </div>

            <button
                className="log-interaction-button"
                type="submit"
            >
                Log Interaction
            </button>

        </form>
    );
}

export default InteractionForm;