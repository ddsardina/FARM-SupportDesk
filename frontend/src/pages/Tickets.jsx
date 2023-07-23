import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { getTickets } from "../features/tickets/ticketSlice"
import Spinner from "../componenets/Spinner"
import TicketItem from "../componenets/TicketItem"

function Tickets() {
    const {tickets} = useSelector((state) => state.tickets)

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getTickets)
    }, [dispatch])

    useEffect(() => {
        dispatch(getTickets())
    }, [dispatch])

    if(!tickets) {
        return <Spinner />
    }


    return (
        <>
            <h1>Tickets</h1>
            <div className='tickets'>
                <div className='ticket-headings'>
                <div>Product</div>
                <div>Status</div>
                <div></div>
                </div>
                {tickets.map((ticket) => (
                <TicketItem key={ticket._id} ticket={ticket} />
                ))}
            </div>
        </>
    )
}

export default Tickets