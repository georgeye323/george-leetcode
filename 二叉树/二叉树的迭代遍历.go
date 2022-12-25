package main

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
	res := make([]int, 0)
	traversal(&res, root)
	return res
}

func traversal(res *[]int, root *TreeNode){
	if root == nil {
		return 
	}
	*res = append(*res, root.Val)
	traversal(res, root.Left)
	traversal(res, root.Right)
}

func main()  {
	
}