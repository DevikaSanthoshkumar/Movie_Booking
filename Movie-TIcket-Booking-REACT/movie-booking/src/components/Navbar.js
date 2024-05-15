import React from 'react';
import { Link } from 'react-router-dom';


function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-dark">
       <Link className="navbar-brand text-light" to="/">Movie Booking</Link>
       <Link className="nav-link  ml-auto text-light" to="/">Home</Link>
       <Link className="nav-link text-light" to="/Admin_Login">Admin</Link>
       <Link className="nav-link text-light" to="/User_Login">User</Link>
    </nav>
  );
}

export default Navbar;






