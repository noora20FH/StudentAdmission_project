import React from "react";
import { Container } from "react-bootstrap";
import ListGroup from "react-bootstrap/ListGroup";

const Contents = () => {
  return (
    <div>
      <div className="contents">
        <Container>
        <ListGroup>
          <ListGroup.Item>Cras justo odio</ListGroup.Item>
          <ListGroup.Item>Dapibus ac facilisis in</ListGroup.Item>
          <ListGroup.Item>Morbi leo risus</ListGroup.Item>
          <ListGroup.Item>Porta ac consectetur ac</ListGroup.Item>
          <ListGroup.Item>Vestibulum at eros</ListGroup.Item>
        </ListGroup>
        </Container>
      </div>
    </div>
  );
};

export default Contents;
