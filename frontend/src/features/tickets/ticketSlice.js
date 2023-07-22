import { createSlice, createAsyncThunk } from "@reduxjs/toolkit"
import ticketService from './ticketService'

const initialState = {
    tickets: [],
    ticket: {},
    isError: false,
    isSuccess: false,
    isLoading: false,
    message: ''
}

// Create New Ticket
export const createTicket = createAsyncThunk(
    'ticket/create', 
    async (ticketData, ThunkAPI) => {
        try {
            const token = ThunkAPI.getState().auth.user.token
            return await ticketService.createTicket(ticketData, token)
        } catch (error) {
            const message = error.response.data.detail

            return ThunkAPI.rejectWithValue(message)
        }
    }
)

// Get User Tickets
export const getTickets = createAsyncThunk(
    'ticket/getAll', 
    async (_, ThunkAPI) => {
        try {
            const token = ThunkAPI.getState().auth.user.token
            return await ticketService.getTickets(token)
        } catch (error) {
            const message = error.response.data.detail

            return ThunkAPI.rejectWithValue(message)
        }
    }
)

export const ticketSlice = createSlice({
    name: 'ticket',
    initialState,
    reducers: {
        reset: (state) => initialState
    },
    extraReducers: (builder) => {
        builder
            .addCase(createTicket.pending, (state) => {
                state.isLoading = true
            })
            .addCase(createTicket.fulfilled, (state) => {
                state.isLoading = false
                state.isSuccess = true
            })
            .addCase(createTicket.rejected, (state, action) => {
                state.isLoading = false
                state.isError = true
                state.message = action.payload
            })
            .addCase(getTickets.pending, (state) => {
                state.isLoading = true
            })
            .addCase(getTickets.fulfilled, (state, action) => {
                state.isLoading = false
                state.isSuccess = true
                state.tickets = action.payload
            })
            .addCase(getTickets.rejected, (state, action) => {
                state.isLoading = false
                state.isError = true
                state.message = action.payload
            })
    }
})

export const {reset} = ticketSlice.actions
export default ticketSlice.reducer