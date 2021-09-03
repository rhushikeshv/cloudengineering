import { Component, OnInit } from '@angular/core';
import { DrawingService } from './drawing.service';

@Component({
  selector: 'app-drawing',
  templateUrl: './drawing.component.html',
  styleUrls: ['./drawing.component.css']
})
export class DrawingComponent implements OnInit {

  private gridApi:any;
  private gridColumnApi:any;
  defaultColDef = {
    resizable: true,
};
  rowData = [

  ];
  columnDefs = [{ field: 'ApprovedBy' }, { field: 'Drawingtitle' }, { field: 'Part' }, {field: 'State'}];


  constructor(private drawingService: DrawingService) {
    this.defaultColDef = { resizable: true };
  }
  sizeToFit() {
    this.gridApi.sizeColumnsToFit();
  }

  autoSizeAll(skipHeader:any) {
    let allColumnIds:any = [];
    this.gridColumnApi.getAllColumns().forEach(function (column:any) {
      allColumnIds.push(column.colId);
    });
    this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
  }

  onGridReady(params:any) {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;
    this.sizeToFit();


  }


  ngOnInit(): void {
    this.drawingService.getDrawings().subscribe((data)=>{
      console.log(data.Items);
      this.rowData = data.Items
    })

  }

}
