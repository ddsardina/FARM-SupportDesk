import { useDebugValue, useEffect } from "react"
import { UseSelector, useDispatch, useSelector } from "react-redux"
import { getTickets, reset } from "../features/tickets/ticketSlice"
import Spinner from "../componenets/Spinner"

function Tickets() {
    const {tickets, isLoading, isSuccess} = useSelector((state) => state.tickets)

    const dispatch = useDispatch()

    useEffect(() => {
        return () => {
            if(isSuccess) {
                dispatch(reset)
            }
        }
    }, [dispatch, isLoading])

    useEffect(() => {
        dispatch(getTickets())
    }, [dispatch])

    if(isLoading) {
        return <Spinner />
    }


    return (
        <div>
            <h1>Tickets</h1>
        </div>
    )
}

export default Tickets