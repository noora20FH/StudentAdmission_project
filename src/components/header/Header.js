import React from "react";
import {Navbar,Nav} from "react-bootstrap";
import Container from 'react-bootstrap/Container';

const Header = () => {
  return (
    <div>
      <div>
        <div className="header">
          <Navbar bg="dark" variant="dark" expand="lg" className="ml-auto">
            <Container fluid>
              <Navbar.Brand href="#">Navbar scroll</Navbar.Brand>
              <Navbar.Toggle aria-controls="navbarScroll" />
              <Navbar.Collapse id="navbarScroll">
                <Nav
                  className="me-auto my-2 my-lg-0"
                  style={{ maxHeight: "100px" }}
                  navbarScroll
                >
                  <Nav.Link href="#action1">Home</Nav.Link>
                  <Nav.Link href="#action2">Link</Nav.Link>
                  <Nav.Link href="#action3">Link</Nav.Link>
                </Nav>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        </div>
      </div>
    </div>
  );
};

export default Header;
