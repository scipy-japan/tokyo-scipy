subroutine ddot_f(a, b, len_a, dot_value)
    implicit none
    
    real(8), intent(in) :: a(len_a)
    real(8), intent(in) :: b(len_a)
    integer, intent(in) :: len_a
    real(8), intent(out) :: dot_value 

    integer :: i
    dot_value = 0.0d0
    do i = 1, len_a
        dot_value = dot_value + a(i) * b(i)
    enddo
end subroutine
