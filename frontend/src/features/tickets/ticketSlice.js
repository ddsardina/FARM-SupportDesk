import { createSlice, createAsyncThunk } from "@reduxjs/toolkit"
import ticketService from './ticketService'

const initialState = {
    tickets: [],
    ticket: {},
}

// Create new ticket
export const createTicket = createAsyncThunk(
    'tickets/create',
    async (ticketData, thunkAPI) => {
        try {
            const token = thunkAPI.getState().auth.user.token
            return await ticketService.createTicket(ticketData, token)
        } catch (error) {
            const message = error.response.data.detail
            return thunkAPI.rejectWithValue(message)
        }
    }
)
  
  // Get user tickets
export const getTickets = createAsyncThunk(
    'tickets/getAll',
    async (_, thunkAPI) => {
        try {
            const token = thunkAPI.getState().auth.user.token
            return await ticketService.getTickets(token)
        } catch (error) {
            const message = error.response.data.detail
            return thunkAPI.rejectWithValue(message)
        }
    }
)
  
  // Get user ticket
export const getTicket = createAsyncThunk(
    'tickets/get',
    async (ticketId, thunkAPI) => {
        try {
            const token = thunkAPI.getState().auth.user.token
            return await ticketService.getTicket(ticketId, token)
        } catch (error) {
            const message = error.response.data.detail
            return thunkAPI.rejectWithValue(message)
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
            .addCase(getTickets.pending, (state) => {
                state.ticket = null
            })
            .addCase(getTickets.fulfilled, (state, action) => {
                state.tickets = action.payload
            })
            .addCase(getTicket.fulfilled, (state, action) => {
                state.ticket = action.payload
            })
    }
})

export const {reset} = ticketSlice.actions
export default ticketSlice.reducer