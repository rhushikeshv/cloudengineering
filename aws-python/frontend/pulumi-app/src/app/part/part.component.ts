import { Component, OnInit } from '@angular/core';
import {PartService} from './part.service';

@Component({
  selector: 'app-part',
  templateUrl: './part.component.html',
  styleUrls: ['./part.component.css']
})
export class PartComponent implements OnInit {

  rowData = [
   
  ];
  columnDefs = [{ field: 'Partname' }, { field: 'Partnumber' }, { field: 'Quantity' }, {field: 'Lifecyclestate'}];

  constructor(private partService: PartService) {}

  ngOnInit(): void {
    this.partService.getParts().subscribe((data) => {
      console.log(data.Items);
      this.rowData = data.Items;
    });
  }



}
