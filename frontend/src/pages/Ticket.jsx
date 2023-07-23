import { useSelector, useDispatch } from "react-redux"
import { useParams } from "react-router-dom"
import { useEffect } from "react"
import { toast } from "react-toastify"
import { getTicket } from "../features/tickets/ticketSlice" 
import Spinner from "../componenets/Spinner"

function Ticket() {
    const { ticket } = useSelector((state) => state.tickets)

    const dispatch = useDispatch()
    const { ticketId } = useParams()

    useEffect(() => {
        dispatch(getTicket(ticketId)).unwrap().catch(toast.error)
    }, [ticketId, dispatch])

    if (!ticket){
        return <Spinner />
    }


    return (
        <div className='ticket-page'>
            <header className='ticket-header'>
                <h2>
                    Ticket ID: {ticket._id}
                    <span className={`status status-${ticket.status}`}>
                        {ticket.status}
                    </span>
                </h2>
                <h3>
                    Date Submitted: {new Date(ticket.timestamp).toLocaleString('en-US')}
                </h3>
                <h3>Product: {ticket.product}</h3>
                <hr />
                <div className='ticket-desc'>
                    <h3>Description of Issue</h3>
                    <p>{ticket.description}</p>
                </div>
            </header>
        </div>
    )
}

export default Ticket