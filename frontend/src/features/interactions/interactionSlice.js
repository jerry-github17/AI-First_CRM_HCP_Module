import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    interactions: [],
    selectedInteraction: null,
    loading: false,
    error: null
};

const interactionSlice = createSlice({
    name: "interactions",
    initialState,
    reducers: {
        addInteraction: (state, action) => {
            state.interactions.push(action.payload);
        },

        setSelectedInteraction: (state, action) => {
            state.selectedInteraction = action.payload;
        },

        clearSelectedInteraction: (state) => {
            state.selectedInteraction = null;
        }
    }
});

export const {
    addInteraction,
    setSelectedInteraction,
    clearSelectedInteraction
} = interactionSlice.actions;

export default interactionSlice.reducer;