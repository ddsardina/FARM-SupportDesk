import {createSlice, createAsyncThunk, createAction} from '@reduxjs/toolkit'
import authService from './authService'

// Get user from local Storage
const user = JSON.parse(localStorage.getItem('user'))

const initialState = {
    user: user ? user : null,
    isLoading: false,
}

// Register New User
export const register = createAsyncThunk(
    'auth/register', 
    async (user, ThunkAPI) => {
        try {
            return await authService.register(user)
        } catch (error) {
            const message = error.response.data.detail
            return ThunkAPI.rejectWithValue(message)
        }
    }
)

// Login User
export const login = createAsyncThunk(
    'auth/login', 
    async (user, ThunkAPI) => {
        try {
            return await authService.login(user)
        } catch (error) {
            const message = error.response.data.detail
            return ThunkAPI.rejectWithValue(message)
        }
    }
)

// Logout user
export const logout = createAction('auth/logout', () => {
    authService.logout()
    return {}
})

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        logout: (state) => {
            state.user = null
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(register.pending, (state) => {
                state.isLoading = true
            })
            .addCase(register.fulfilled, (state, action) => {
                state.isLoading = false
                state.user = action.payload
            })
            .addCase(register.rejected, (state, action) => {
                state.isLoading = false
            })
            .addCase(login.pending, (state) => {
                state.isLoading = true
            })
            .addCase(login.fulfilled, (state, action) => {
                state.isLoading = false
                state.user = action.payload
            })
            .addCase(login.rejected, (state, action) => {
                state.isLoading = false
            })
    }
})

export default authSlice.reducer