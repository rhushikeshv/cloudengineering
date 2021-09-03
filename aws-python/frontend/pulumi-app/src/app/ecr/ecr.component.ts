import { Component, OnInit } from '@angular/core';
import { EcrService } from './ecr.service';

@Component({
  selector: 'app-ecr',
  templateUrl: './ecr.component.html',
  styleUrls: ['./ecr.component.css']
})
export class EcrComponent implements OnInit {

  private gridApi:any;
  private gridColumnApi:any;
   defaultColDef = {
    resizable: true

};

  rowData = [

  ];
  columnDefs = [{ field: 'Reason for Change' }, { field: 'Enggchange' }, { field: 'Impacted Parts' },
  {field: 'Problem Description'}];
  gridOptions:any = { defaultColDef: { resizable: true, }, columnDefs: this.columnDefs, rowData: this.rowData, colResizeDefault: 'shift', };

  constructor(private ecrService: EcrService) { }

  ngOnInit(): void {
    this.ecrService.getEcrs().subscribe((data)=>{
      console.log(data.Items)
      this.rowData = data.Items
    })

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
    this.autoSizeAll(false);


  }

}
