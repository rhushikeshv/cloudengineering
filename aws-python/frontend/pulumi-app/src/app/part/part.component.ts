import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-part',
  templateUrl: './part.component.html',
  styleUrls: ['./part.component.css']
})
export class PartComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  rowData = [
    { make: "Toyota", model: "Celica", price: 35000 },
    { make: "Ford", model: "Mondeo", price: 32000 },
    { make: "Porsche", model: "Boxter", price: 72000 }
  ];
  columnDefs = [{ field: "make" }, { field: "model" }, { field: "price" }];

}
