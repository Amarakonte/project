import { Component, OnInit } from '@angular/core';
import { LINKS } from 'src/app/_commons/datas';
import { Link } from 'src/app/_commons/models/link';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {
  constructor() {}

  public links: Link[] = LINKS;

  ngOnInit(): void {}
}
