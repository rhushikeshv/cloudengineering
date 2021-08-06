import { Component, OnInit } from '@angular/core';
import { DrawingService } from './drawing.service';

@Component({
  selector: 'app-drawing',
  templateUrl: './drawing.component.html',
  styleUrls: ['./drawing.component.css']
})
export class DrawingComponent implements OnInit {

  rowData = [
    
  ];
  columnDefs = [{ field: 'ApprovedBy' }, { field: 'Drawingtitle' }, { field: 'Part' }, {field: 'State'}];

  constructor(private drawingService: DrawingService) { }

  ngOnInit(): void {

    this.drawingService.getDrawings().subscribe((data)=>{
      console.log(data.Items);
      this.rowData = data.Items
    })
  }

}
