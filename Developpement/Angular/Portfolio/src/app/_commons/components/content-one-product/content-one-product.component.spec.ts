import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentOneProductComponent } from './content-one-product.component';

describe('ContentOneProductComponent', () => {
  let component: ContentOneProductComponent;
  let fixture: ComponentFixture<ContentOneProductComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ContentOneProductComponent],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentOneProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
