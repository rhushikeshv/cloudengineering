import { Component, OnInit } from '@angular/core';
import { EcrService } from './ecr.service';

@Component({
  selector: 'app-ecr',
  templateUrl: './ecr.component.html',
  styleUrls: ['./ecr.component.css']
})
export class EcrComponent implements OnInit {

  rowData = [
    
  ];
  columnDefs = [{ field: 'Reason for Change' }, { field: 'Enggchange' }, { field: 'Impacted Parts' }, 
  {field: 'Problem Description'}];

  constructor(private ecrService: EcrService) { }

  ngOnInit(): void {
    this.ecrService.getEcrs().subscribe((data)=>{
      console.log(data.Items)
      this.rowData = data.Items
    })

  }

}
