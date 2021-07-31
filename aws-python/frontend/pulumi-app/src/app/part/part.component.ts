import { Component, OnInit } from '@angular/core';
import {PartService} from './part.service';

@Component({
  selector: 'app-part',
  templateUrl: './part.component.html',
  styleUrls: ['./part.component.css']
})
export class PartComponent implements OnInit {

  rowData = [
    { make: 'Toyota', model: 'Celica', price: 35000 },
    { make: 'Ford', model: 'Mondeo', price: 32000 },
    { make: 'Porsche', model: 'Boxter', price: 72000 }
  ];
  columnDefs = [{ field: 'make' }, { field: 'model' }, { field: 'price' }];

  constructor(private partService: PartService) {}

  ngOnInit(): void {
    this.partService.getParts().subscribe((data) => {
      console.log(data);
    });
  }



}
